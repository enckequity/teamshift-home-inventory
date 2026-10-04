/** Change translated display names while preserving URLs and persisted identifiers. */
export const brandMessage = (message: string): string =>
  message
    .replace(/(?<![\w/.-])Home[Bb]ox(?=-)/g, "TeamShift")
    .replace(/(?<![\w/.-])homebox(?![\w/-]|\.(?=[\w-]))/gi, "TeamShift");
