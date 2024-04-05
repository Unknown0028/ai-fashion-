document.getElementById("recommendation-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const style = document.getElementById("style").value;
    const size = document.getElementById("size").value;
    const occasion = document.getElementById("occasion").value;
    // Send the data to the backend for processing and retrieve recommendations
    // For demonstration purposes, let's assume recommendations are fetched from an API
    fetchRecommendations(style, size, occasion);
});

function fetchRecommendations(style, size, occasion) {
    // Make an API call to your backend with the provided data
    // For demonstration purposes, let's assume the API returns recommendations as JSON
    const recommendations = [
        { name: "Item 1", price: "$50" },
        { name: "Item 2", price: "$60" },
        { name: "Item 3", price: "$70" }
    ];

    // Display recommendations on the UI
    displayRecommendations(recommendations);
}

function displayRecommendations(recommendations) {
    const recommendationsContainer = document.getElementById("recommendations");
    recommendationsContainer.innerHTML = "<h2>Recommendations:</h2>";
    recommendations.forEach(item => {
        const recommendationElement = document.createElement("div");
        recommendationElement.innerHTML = `<strong>${item.name}</strong> - ${item.price}`;
        recommendationsContainer.appendChild(recommendationElement);
    });
}
