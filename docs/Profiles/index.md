---
title: Home
date: 2023-10-06
---

This section contains the list of all the profiles that are available in the system. The list is sorted by the profile name.

Review the flowchart to determine which profile is best suited for your needs.
![flowchart](flowchart.png)

<form id="deviceSelectionForm">
    <label for="deviceType">Select your device type:</label>
    <select id="deviceType">
        <option value="tv">TV</option>
        <option value="phone">Phone</option>
        <option value="computer">Computer</option>
        <!-- Add other device types as needed -->
    </select>

    <label for="hdrCompliant">Is your device HDR compliant?</label>
    <select id="hdrCompliant">
        <option value="yes">Yes</option>
        <option value="no">No</option>
        <option value="unknown">I don't know</option>
    </select>

    <label for="fileSize">Preferred file size:</label>
    <select id="fileSize">
        <option value="small">Up to 1GB</option>
        <option value="medium">1GB - 5GB</option>
        <option value="large">More than 5GB</option>
    </select>

    <input type="submit" value="Submit">

</form>

<div id="result"></div>

<style>
#deviceSelectionForm {
font-family: Arial, sans-serif;
margin: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

select {
    margin-bottom: 10px;
    padding: 5px;
}

input[type="submit"] {
    padding: 5px 10px;
    background-color: #4CAF50;
    border: none;
    color: white;
    cursor: pointer;
}

</style>

<script>
    document.getElementById('deviceSelectionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const deviceType = document.getElementById('deviceType').value;
    const hdrCompliant = document.getElementById('hdrCompliant').value;
    const fileSize = document.getElementById('fileSize').value;

    let resultLink;

    // Example logic (you can adjust as per your needs)
    if (deviceType === 'tv' && hdrCompliant === 'yes' && fileSize === 'large') {
        resultLink = '/path_for_large_hdr_tv.html';
    } else if (deviceType === 'phone' && fileSize === 'small') {
        resultLink = '/path_for_small_phone.html';
    }
    // ... Add more conditions as needed ...

    const resultDiv = document.getElementById('result');
    if (resultLink) {
        resultDiv.innerHTML = `<a href="${resultLink}">Click here for your recommendation</a>`;
    } else {
        resultDiv.textContent = "Sorry, we couldn't find a recommendation for your combination.";
    }
});

</script>
