<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Store</title>
</head>
<body>

<h1>Welcome to the E-commerce Store</h1>
<p>This is the landing page for our e-commerce application.</p>

<h2>Add Item to Cart</h2>
<input type="text" id="item" placeholder="Item Name" />
<input type="number" id="price" placeholder="Price" />
<button onclick="addToCart('user1')">Add to Cart</button>

<h2>Get Cart</h2>
<button onclick="getCart('user1')">View Cart</button>

<h2>Checkout</h2>
<input type="text" id="discountCode" placeholder="Discount Code (optional)" />
<button onclick="checkout('user1')">Checkout</button>

<h2>Generate Discount Code</h2>
<button onclick="generateDiscount()">Generate Discount Code</button>

<h2>Admin Stats</h2>
<button onclick="getAdminStats()">View Admin Stats</button>

<div id="result"></div>

<script>
async function addToCart(userId) {
  const itemName = document.getElementById('item').value;
  const itemPrice = parseFloat(document.getElementById('price').value);
  
  const response = await fetch(`/api/cart/${userId}/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ item: itemName, price: itemPrice })
  });

  const data = await response.json();
  document.getElementById('result').innerText = JSON.stringify(data);
}

async function getCart(userId) {
  const response = await fetch(`/api/cart/${userId}/`);
  
  const data = await response.json();
  document.getElementById('result').innerText = JSON.stringify(data);
}

async function checkout(userId) {
  const discountCode = document.getElementById('discountCode').value;

  const response = await fetch(`/api/checkout/${userId}/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ discount_code: discountCode })
  });

  const data = await response.json();
  document.getElementById('result').innerText = JSON.stringify(data);
}

async function generateDiscount() {
  const response = await fetch(`/api/generate_discount/`, { method: 'POST' });
  
  const data = await response.json();
  document.getElementById('result').innerText = JSON.stringify(data);
}

async function getAdminStats() {
  const response = await fetch(`/api/admin/stats/`);
  
  const data = await response.json();
  document.getElementById('result').innerText = JSON.stringify(data);
}
</script>

</body>
</html>