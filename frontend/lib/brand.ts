// TeamShift presentation only: preserve technical IDs, URLs and user data.
export const brandMessage = (message: string): string =>
  message.replace(/(?<![\w/.-])homebox(?![\w/.-])/gi, "TeamShift");
