function placeOrder(){

    fetch("http://127.0.0.1:8000/api/orders/place/", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        }

    })

    .then(response => response.json())

    .then(data => {

        alert("Order Placed Successfully");

        console.log(data);

        window.location.href = "/";

    })

    .catch(error => {

        console.log(error);

    });

}