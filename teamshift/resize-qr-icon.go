// Rebuild the native QR icon from the canonical TeamShift PWA asset.
package main

import (
	"image"
	"image/png"
	"os"
)

func main() {
	in, err := os.Open("frontend/public/pwa-192x192.png")
	if err != nil {
		panic(err)
	}
	src, err := png.Decode(in)
	in.Close()
	if err != nil {
		panic(err)
	}
	out := image.NewRGBA(image.Rect(0, 0, 50, 50))
	bounds := src.Bounds()
	for y := 0; y < 50; y++ {
		for x := 0; x < 50; x++ {
			out.Set(x, y, src.At(bounds.Min.X+x*bounds.Dx()/50, bounds.Min.Y+y*bounds.Dy()/50))
		}
	}
	f, err := os.Create("backend/app/api/handlers/v1/assets/QRIcon.png")
	if err != nil {
		panic(err)
	}
	if err = png.Encode(f, out); err != nil {
		panic(err)
	}
	if err = f.Close(); err != nil {
		panic(err)
	}
}
