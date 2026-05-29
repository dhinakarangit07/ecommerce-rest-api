console.log("APP JS LOADED");

async function loadProducts() {

    const response = await fetch("http://127.0.0.1:8000/api/products/");

    const products = await response.json();

    const container = document.getElementById("products-container");

    container.innerHTML = "";

    products.forEach(product => {

        container.innerHTML += `

        <div class="col-md-4 mb-4">

            <div class="card product-card h-100">

                <img src="${product.image}"
                     class="card-img-top product-image">

                <div class="card-body">

                    <h5 class="card-title">
                        ${product.name}
                    </h5>

                    <p class="card-text">
                        ₹${product.price}
                    </p>

                    <a href="/product/${product.id}/"
                       class="btn btn-primary">
                       View Product
                    </a>

                </div>

            </div>

        </div>

        `;
    });
}

loadProducts();