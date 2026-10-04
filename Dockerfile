# Node dependencies stage
FROM public.ecr.aws/docker/library/node:22-alpine AS frontend-dependencies
WORKDIR /app

# Install pnpm 10 (latest stable, works reliably in Alpine)
RUN npm install -g pnpm@10

# Copy package.json and lockfile to leverage caching
COPY frontend/package.json frontend/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

# Build Nuxt (frontend) stage
FROM public.ecr.aws/docker/library/node:22-alpine AS frontend-builder
WORKDIR /app

# Install pnpm 10 (latest stable)
RUN npm install -g pnpm@10

# Compile source with a temporary dependency-stage mount; avoid duplicating module layers.
COPY frontend . 
RUN --mount=type=bind,from=frontend-dependencies,source=/app/node_modules,target=/app/node_modules,rw pnpm build

# Go dependencies stage
FROM public.ecr.aws/docker/library/golang:alpine AS builder-dependencies
WORKDIR /go/src/app

# Copy go.mod and go.sum for better caching
COPY ./backend/go.mod ./backend/go.sum ./
RUN go mod download

# Build API stage
FROM public.ecr.aws/docker/library/golang:alpine AS builder
ARG TARGETOS
ARG TARGETARCH
ARG BUILD_TIME
ARG COMMIT
ARG VERSION

# Install necessary build tools
RUN apk update && \
    apk upgrade && \
    apk add --no-cache git build-base gcc g++ && \
    if [ "$TARGETARCH" != "arm" ] || [ "$TARGETARCH" != "riscv64" ]; then apk --no-cache add libwebp libavif libheif libjxl; fi

WORKDIR /go/src/app

# Copy source; module dependencies are mounted only during compilation.
COPY ./backend .

# Clear old public files and copy new ones from frontend build
RUN rm -rf ./app/api/public
COPY --from=frontend-builder /app/.output/public ./app/api/static/public

# Use cache for Go build artifacts
RUN --mount=type=bind,from=builder-dependencies,source=/go/pkg/mod,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    if [ "$TARGETARCH" = "arm" ] || [ "$TARGETARCH" = "riscv64" ];  \
    then echo "nodynamic" $TARGETOS $TARGETARCH; CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build \
        -ldflags "-s -w -X main.commit=$COMMIT -X main.buildTime=$BUILD_TIME -X main.version=$VERSION" \
        -tags nodynamic -o /go/bin/api -v ./app/api/*.go; \
    else \
         echo $TARGETOS $TARGETARCH; CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build \
        -ldflags "-s -w -X main.commit=$COMMIT -X main.buildTime=$BUILD_TIME -X main.version=$VERSION" \
        -o /go/bin/api -v ./app/api/*.go; \
    fi

# Production stage
FROM public.ecr.aws/docker/library/alpine:latest
ENV HBOX_MODE=production
ENV HBOX_STORAGE_CONN_STRING=file:///?no_tmp_dir=true
ENV HBOX_STORAGE_PREFIX_PATH=data
ENV HBOX_DATABASE_SQLITE_PATH=/data/homebox.db?_pragma=busy_timeout=2000&_pragma=journal_mode=WAL&_fk=1&_time_format=sqlite

# Install necessary runtime dependencies
RUN apk --no-cache add ca-certificates wget mosquitto-clients && \
    if [ "$TARGETARCH" != "arm" ] || [ "$TARGETARCH" != "riscv64" ]; then apk --no-cache add libwebp libavif libheif libjxl; fi

# Create application directory and copy over built Go binary
RUN mkdir /app
COPY --from=builder /go/bin/api /app
RUN chmod +x /app/api

# Labels and configuration for the final image
LABEL Name=teamshift-home-inventory Version=0.0.1
LABEL org.opencontainers.image.source="https://github.com/enckequity/teamshift-home-inventory"

# Expose necessary ports for Homebox
EXPOSE 7745
WORKDIR /app

# Healthcheck configuration
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD [ "wget", "--no-verbose", "--tries=1", "-O", "-", "http://localhost:7745/api/v1/status" ]

# Persist volume
VOLUME [ "/data" ]

# Entrypoint and CMD
ENTRYPOINT [ "/app/api" ]
CMD [ "/data/config.yml" ]
