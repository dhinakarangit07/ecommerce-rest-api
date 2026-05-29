const cartItems = document.getElementById("cart-items");

const totalElement = document.getElementById("cart-total");

let total = 0;


fetch("http://127.0.0.1:8000/api/cart/")
.then(response => response.json())

.then(data => {

    data.forEach(item => {

        total += item.product.price * item.quantity;

        cartItems.innerHTML += `

        <div class="col-md-4 mb-4">

            <div class="card shadow">

                <img src="http://127.0.0.1:8000${item.product.image}"
                     class="card-img-top product-img">

                <div class="card-body">

                    <h5>${item.product.name}</h5>

                    <p>Quantity: ${item.quantity}</p>

                    <p class="price">
                        ₹${item.product.price}
                    </p>

                    <button class="btn btn-danger"
                            onclick="removeCart(${item.id})">

                        Remove

                    </button>

                </div>

            </div>

        </div>

        `;

    });

    totalElement.innerText = total;

})

.catch(error => {

    console.log(error);

});



function removeCart(cartId){

    fetch(`http://127.0.0.1:8000/api/cart/${cartId}/`, {

        method: "DELETE"

    })

    .then(response => {

        alert("Item Removed");

        location.reload();

    });

}