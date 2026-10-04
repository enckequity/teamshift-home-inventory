/** Existing inventory labels use immutable item IDs; blank labels retain asset lookup. */
export const labelDestination = (baseURL: string, assetID: string, entityID?: string): string => {
  const origin = baseURL.trim().replace(/\/$/, "");
  return entityID ? `${origin}/item/${entityID}` : `${origin}/a/${assetID}`;
};
