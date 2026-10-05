/** Change translated display names while preserving URLs and persisted identifiers. */
export const brandMessage = (message: string): string =>
  message
    .replace(/(?<![\w/.-])Home[Bb]ox(?=-)/g, "TeamShift")
    .replace(/(?<![\w/.-])homebox(?![\w/-]|\.(?=[\w-]))/gi, "TeamShift");

/** Link the displayed build to its corresponding modified source; never interpolate arbitrary URLs. */
export const buildSourceUrl = (commit: string): string => {
  const repository = "https://github.com/enckequity/teamshift-home-inventory";
  return /^[a-f0-9]{7,40}$/i.test(commit) ? `${repository}/commit/${commit}` : repository;
};
