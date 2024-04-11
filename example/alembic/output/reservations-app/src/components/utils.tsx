import { DefaultApi } from "../api";
import { Configuration } from "../api";

const basePath = "http://localhost:8000";

const parseField = (field: string, type: string) => {
  switch (type) {
    case "string":
      return field;
    case "number":
      return Number(field);
    case "boolean":
      return field === "true";
    case "date":
      return new Date(field);
    case "datetime":
      return new Date(field);
    case "array":
      return field.split(",").map((item) => (item as string).trim());
    case "list":
      return field.split(",").map((item) => (item as string).trim());
    case "object":
      return JSON.parse(field);
    default:
      return field;
  }
};

const getAPIClient = () => {
  const configuration = new Configuration({
    basePath: basePath,
  });
  return new DefaultApi(configuration);
};

export { getAPIClient, parseField };
