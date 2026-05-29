const productList = document.getElementById("product-list");

fetch("http://127.0.0.1:8000/api/products/")
.then(response => response.json())
.then(data => {

    data.forEach(product => {

        productList.innerHTML += `

        <div class="col-md-4 mb-4">

            <div class="card shadow">

                <img src="http://127.0.0.1:8000${product.image}"
                     class="card-img-top product-img">

                <div class="card-body">

                    <h5>${product.name}</h5>

                    <p>${product.description}</p>

                    <p class="price">₹${product.price}</p>

                    <a href="/product/${product.id}/"
                       class="btn btn-dark">
                       View
                    </a>

                    <button class="btn btn-primary"
                            onclick="addToCart(${product.id})">
                        Add Cart
                    </button>

                </div>

            </div>

        </div>

        `;
    });

})
.catch(error => {
    console.log(error);
});


// GET CSRF TOKEN
function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {

        const cookies = document.cookie.split(';');

        for (let i = 0; i < cookies.length; i++) {

            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {

                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );

                break;
            }
        }
    }

    return cookieValue;
}


// ADD TO CART
function addToCart(productId){

    const csrftoken = getCookie('csrftoken');

    fetch("http://127.0.0.1:8000/api/cart/", {

        method: "POST",

        credentials: "same-origin",

        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },

        body: JSON.stringify({
            product: productId,
            quantity: 1
        })

    })
    .then(response => response.json())
    .then(data => {

        alert("Product Added To Cart");

        console.log(data);

    })
    .catch(error => {
        console.log(error);
    });

}