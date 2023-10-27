async function fetchIt(type: string, url: string, requestBody: object = {}, header: object = { 'Content-Type': 'application/json' }) {
    const settings: object = header;
    let response;
    if (Object.keys(requestBody).length === 0) {
        response = await window.fetch(url, {
            method: type,
            headers: settings as HeadersInit
        });
    }
    else if (type === "GET") {
        let url1 = new URL(url);
        requestBody = {
            hry: 'a',
        }
        let k: keyof typeof requestBody;
        for (k in requestBody) {
            url1.searchParams.append(k, requestBody[k])
        }
        response = await window.fetch(url1, {
            method: type,
            headers: settings as HeadersInit,
        });
    }
    else if (type === "POST") {
        await window.fetch(url, {
            method: type,
            headers: settings as HeadersInit,
            body: JSON.stringify(requestBody),
        });
    }
    else {
        response = await window.fetch(url, {
            method: type,
            headers: settings as HeadersInit
        });
    }
    if (response === undefined) {
        response = await window.fetch(url, {
            method: type,
            headers: settings as HeadersInit
        });
    }
    
    try {
        return [await response.json(), await response.status];
    }
    catch (e) {
        return 1;
    }
}

export default fetchIt;