//function to parse data
function parseData(data) {
    // Check if data is an array
    if (!Array.isArray(data)) {
        throw new Error("Input data must be an array");
    }

    // Map through the array and parse each item
    return data.map(item => {
        if (typeof item !== 'object' || item === null) {
            throw new Error("Each item in the array must be a non-null object");
        }
        
        // Assuming each item has 'name' and 'value' properties
        return {
            name: item.name || "Unknown",
            value: item.value || 0
        };
    });
}


// parse url
function parseUrl(url) {
    // Check if the input is a valid URL
    try {
        const parsedUrl = new URL(url);
        return {
            protocol: parsedUrl.protocol,
            host: parsedUrl.host,
            pathname: parsedUrl.pathname,
            searchParams: Object.fromEntries(parsedUrl.searchParams.entries())
        };
    } catch (error) {
        throw new Error("Invalid URL");
    }
}