function sendHttpRequest() {
    var API_URL = "https://api.quantumnumbers.anu.edu.au";
    var API_KEY = "hDQgnGciJ13t0zOZF1MuD1PpJ4TsnHb63YAgjJgH";
    var arrayLength = 1024; // Replace with your desired values
    var dataType = "uint8"; // Replace with your desired values
    //var blockSize = 1; // Replace with your desired values

    var url = API_URL + "?length=" + arrayLength + "&type=" + dataType;// + "&size=" + blockSize;

    // Send the HTTP GET request
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.setRequestHeader("x-api-key", API_KEY);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = xhr.responseText;
            outlet(0, response); // Send the response to a Max outlet
        }
    };

    xhr.send();
}

sendHttpRequest();