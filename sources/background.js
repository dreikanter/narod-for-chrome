chrome.webRequest.onBeforeSendHeaders.addListener(
    function(info) {
        var headers = info.requestHeaders;
        headers.forEach(function(header, i) {
            if (header.name.toLowerCase() == 'user-agent') {
                header.value = header.value + ' YB/7.5.0';
            }
        });
        return {requestHeaders: headers};
    },
    {
        urls: [
            "http://narod.ru/disk/*",
            "http://narod.yandex.ru/*"
        ],
        types: [
            "main_frame",
            "sub_frame"
        ]
    },
    [ "blocking", "requestHeaders" ]
);
