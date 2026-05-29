const path = window.location.pathname;
const productId = path.split("/")[2];

fetch(`/api/products/${productId}/`)
.then(response => response.json())
.then(product => {

    document.getElementById("product-detail").innerHTML = `
    
        <div class="col-md-6">
            <img src="${product.image}" class="img-fluid">
        </div>

        <div class="col-md-6">

            <h2>${product.name}</h2>

            <p>${product.description}</p>

            <h4>₹ ${product.price}</h4>

            <button class="btn btn-success mt-3">
                Add To Cart
            </button>

        </div>
    
    `;
})
.catch(error => console.log(error));