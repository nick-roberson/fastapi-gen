import { Configuration } from "../api";
import { DefaultApi } from "../api";
{% for model in config.models %}
import { {{ model.name }}Api } from "../api";
{% endfor %}

const basePath = "http://localhost:8000";

// Helper function to parse fields based on their type prior to sending to the API
const parseField = (field: string, type: string) => {
    switch (type) {
        case 'string':
            return field;
        case 'number':
            return Number(field);
        case 'boolean':
            return field === 'true';
        case 'date':
            return new Date(field);
        case 'datetime':
            return new Date(field);
        case 'array':
            return field.split(',').map(item => (item as string).trim());
        case 'list':
            return field.split(',').map(item => (item as string).trim());
        case 'object':
            return JSON.parse(field);
        default:
            return field;
    }
}

{% for model in config.models %}
// Fetch API client for {{ model.name }}
const get{{ model.name }}APIClient = () => {
    const apiConfig = new Configuration({
        basePath: basePath
    });
    return new {{ model.name }}Api(apiConfig);
}
{% endfor %}

// Export all API clients and utility functions
export {
    {% for model in config.models %}
    get{{ model.name }}APIClient,
    {% endfor %}
    parseField
}
