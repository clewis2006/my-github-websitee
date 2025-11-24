<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>CL — Athletic Apparel by Christian Lewis</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#fafafa; --text:#0f1724; --muted:#6b7280; --accent:#111827; --accent-2:#ff4d4d; --card:#fff;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:'Inter',system-ui;color:var(--text);background:var(--bg);-webkit-font-smoothing:antialiased}
  a{color:inherit;text-decoration:none} img{max-width:100%;display:block}

  /* Header */
  header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,0.96);backdrop-filter:blur(6px);border-bottom:1px solid rgba(15,23,36,0.06)}
  .nav{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:12px 18px;gap:12px}
  .logo{background:var(--accent);color:#fff;width:48px;height:48px;display:grid;place-items:center;border-radius:10px;font-weight:800;font-size:18px}
  .brand{display:flex;align-items:center;gap:12px}
  .brand .name{font-weight:800}
  .searchbar{flex:1;max-width:640px;display:flex;align-items:center;gap:8px;padding:6px 8px;border-radius:10px;background:#fff;box-shadow:0 6px 18px rgba(2,6,23,0.04)}
  .searchbar input{border:0;outline:none;padding:10px;font-size:14px;width:100%;background:transparent}
  .navlinks{display:flex;gap:12px;align-items:center}
  .pill{padding:8px 12px;border-radius:999px;background:rgba(17,24,39,0.04);font-weight:700;cursor:pointer}
  .btn{background:var(--accent);color:white;border:none;border-radius:10px;padding:10px 14px;font-weight:700;cursor:pointer}
  .btn.ghost{background:transparent;border:1px solid rgba(15,23,36,0.06);color:var(--accent)}

  /* hero */
  .hero{max-width:1200px;margin:30px auto;display:grid;grid-template-columns:1fr 360px;gap:24px;padding:0 18px;align-items:center}
  .hero-card{background:#fff;border-radius:16px;padding:30px;box-shadow:0 20px 40px rgba(2,6,23,0.06)}
  .hero-card h1{margin:0 0 12px;font-size:34px}
  .hero-card p{margin:0;color:var(--muted)}
  .hero-side img{width:100%;border-radius:12px;box-shadow:0 10px 30px rgba(2,6,23,0.06)}

  /* controls */
  .controls{max-width:1200px;margin:20px auto;padding:0 18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
  .categories{display:flex;gap:8px;flex-wrap:wrap}
  .sort{margin-left:auto;display:flex;gap:8px;align-items:center}

  /* product grid */
  .container{max-width:1200px;margin:0 auto;padding:0 18px 60px}
  .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:12px}
  .card{background:var(--card);border-radius:12px;padding:10px;border:1px solid rgba(15,23,36,0.04);transition:transform .18s,box-shadow .18s;overflow:hidden}
  .card:hover{transform:translateY(-6px);box-shadow:0 30px 60px rgba(2,6,23,0.06)}
  .card .img{height:220px;border-radius:10px;overflow:hidden;display:grid;place-items:center;background:#f3f4f6}
  .card .meta{padding:10px 2px}
  .price{font-weight:800;font-size:16px}
  .muted{color:var(--muted);font-size:13px}

  /* drawer cart */
  .cart-btn{position:relative}
  .cart-count{position:absolute;right:-6px;top:-6px;background:var(--accent-2);color:white;border-radius:50%;width:20px;height:20px;display:grid;place-items:center;font-size:12px;font-weight:700;display:none}
  .drawer{position:fixed;right:18px;top:72px;width:380px;max-width:calc(100% - 36px);background:var(--card);border-radius:12px;padding:14px;box-shadow:0 40px 120px rgba(2,6,23,0.18);z-index:80;transform:translateY(-10px);opacity:0;pointer-events:none;transition:opacity .18s,transform .18s}
  .drawer.open{transform:translateY(0);opacity:1;pointer-events:auto}
  .cart-item{display:flex;gap:10px;padding:8px 0;border-bottom:1px dashed rgba(15,23,36,0.04)}
  .cart-item img{width:64px;height:64px;object-fit:cover;border-radius:8px}
  .cart-footer{display:flex;justify-content:space-between;align-items:center;margin-top:12px}

  /* modal */
  .modal-backdrop{position:fixed;inset:0;display:none;place-items:center;background:rgba(2,6,23,0.55);z-index:100}
  .modal{width:92%;max-width:1000px;background:var(--card);border-radius:12px;padding:18px;display:grid;grid-template-columns:1fr 360px;gap:18px}
  .modal .images{min-height:360px;display:grid;align-items:center;justify-items:center}
  .thumbs{display:flex;gap:8px;margin-top:8px}
  .thumbs img{width:60px;height:60px;object-fit:cover;border-radius:8px;cursor:pointer;border:2px solid transparent}
  .thumbs img.active{border-color:var(--accent)}

  /* responsive */
  @media(max-width:1100px){.grid{grid-template-columns:repeat(3,1fr)} .hero{grid-template-columns:1fr 300px}}
  @media(max-width:860px){.grid{grid-template-columns:repeat(2,1fr)} .hero{grid-template-columns:1fr} .modal{grid-template-columns:1fr}}
  @media(max-width:480px){.grid{grid-template-columns:1fr} .searchbar{display:none}}
  footer{background:#111827;color:white;padding:28px;text-align:center;margin-top:30px}
</style>
</head>
<body>

<header>
  <div class="nav">
    <div class="brand" style="gap:12px">
      <div class="logo">CL</div>
      <div>
        <div class="name">Christian Lewis</div>
        <div class="muted">CL — Athletic Apparel</div>
      </div>
    </div>

    <div class="searchbar" role="search" aria-label="Site search">
      <svg style="width:18px;height:18px;opacity:.6" viewBox="0 0 24 24"><path fill="currentColor" d="M9.5,3A6.5,6.5 0 1,1 3,9.5A6.5,6.5 0 0,1 9.5,3M21,21L15.5,15.5"/></svg>
      <input id="searchInput" placeholder="Search products, e.g. hoodie, shoes..." aria-label="Search products">
      <button class="btn ghost" id="clearSearch">Clear</button>
    </div>

    <div style="display:flex;gap:10px;align-items:center">
      <nav class="navlinks">
        <a href="#collections">Shop</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
      </nav>

      <div class="cart-btn" aria-hidden="false">
        <button class="btn" id="cartToggle">Cart 🛒</button>
        <div class="cart-count" id="cartCount">0</div>
      </div>
    </div>
  </div>
</header>

<section class="hero">
  <div class="hero-card">
    <h1>CL — Performance meets everyday style.</h1>
    <p>Designed by Christian Lewis. Functional materials, modern fits — for people who move.</p>
    <div style="margin-top:18px;display:flex;gap:8px">
      <a href="#collections" class="btn">Shop Collections</a>
      <a href="#collections" class="btn ghost">Browse All</a>
    </div>
  </div>
  <div class="hero-side">
    <img src="https://source.unsplash.com/featured/?athlete,training,apparel" alt="CL collection">
  </div>
</section>

<!-- Controls -->
<div class="controls">
  <div class="categories" id="categoryFilters">
    <div class="pill" data-cat="all">All</div>
    <div class="pill" data-cat="hoodies">Hoodies</div>
    <div class="pill" data-cat="sweatshirts">Sweatshirts</div>
    <div class="pill" data-cat="sweatpants">Sweatpants</div>
    <div class="pill" data-cat="shirts">Shirts</div>
    <div class="pill" data-cat="shoes">Shoes</div>
  </div>

  <div class="sort">
    <label for="sortSel" class="muted">Sort</label>
    <select id="sortSel" style="padding:8px;border-radius:8px;border:1px solid rgba(15,23,36,0.06);margin-left:8px">
      <option value="featured">Featured</option>
      <option value="price-asc">Price: Low → High</option>
      <option value="price-desc">Price: High → Low</option>
      <option value="alpha">A → Z</option>
    </select>
  </div>
</div>

<!-- Product grid -->
<div class="container" id="collections">
  <h2>Products</h2>
  <div class="grid" id="productGrid" aria-live="polite"></div>
</div>

<!-- About -->
<div class="container" id="about">
  <h2>About CL</h2>
  <p>Founded by <strong>Christian Lewis</strong>, CL bridges performance and everyday wear. We use durable materials and modern silhouettes so you look and feel great whether training or on the go.</p>
</div>

<!-- Contact -->
<div class="container" id="contact">
  <h2>Contact</h2>
  <p>Get in touch:</p>
  <ul style="list-style:none;padding:0;line-height:1.8">
    <li>📧 <a href="mailto:clewis8423@gmail.com">clewis8423@gmail.com</a></li>
    <li>📱 <a href="tel:8048924035">804-892-4035</a></li>
  </ul>
</div>

<!-- Footer -->
<footer>
  <div><strong>© 2025 Christian Lewis — CL Athletic Apparel</strong></div>
  <div style="margin-top:8px">Built as a demo storefront — replace with your real CMS & payments when ready.</div>
</footer>

<!-- Cart Drawer -->
<div id="cartDrawer" class="drawer" aria-hidden="true">
  <h3>Cart</h3>
  <div id="cartItems" style="max-height:420px;overflow:auto"></div>
  <div class="cart-footer">
    <div>
      <div style="font-size:12px;color:var(--muted)">Subtotal</div>
      <div style="font-weight:800" id="cartTotal">$0.00</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:8px">
      <button class="btn" id="checkoutBtn">Checkout</button>
      <button class="btn ghost" id="clearCartBtn">Clear</button>
    </div>
  </div>
</div>

<!-- Product Modal -->
<div id="modalBackdrop" class="modal-backdrop" role="dialog" aria-modal="true">
  <div class="modal" role="document" aria-labelledby="modalTitle">
    <div>
      <div class="images" id="modalImages">
        <img id="modalMainImg" src="" alt="Product image" style="width:100%;height:360px;object-fit:cover;border-radius:10px">
        <div class="thumbs" id="modalThumbs"></div>
      </div>
    </div>
    <div>
      <div style="display:flex;justify-content:space-between;align-items:center">
        <h3 id="modalTitle">Product</h3>
        <div style="font-weight:800" id="modalPrice">$0</div>
      </div>
      <div style="color:var(--muted)" id="modalCategory">Category</div>
      <p id="modalDesc" style="margin-top:12px;color:var(--muted)">Description</p>

      <div style="margin-top:12px">
        <label class="muted-small">Size</label>
        <div id="sizeOptions" style="display:flex;gap:8px;margin-top:8px"></div>
      </div>

      <div style="margin-top:12px">
        <label class="muted-small">Color</label>
        <div id="colorOptions" style="display:flex;gap:8px;margin-top:8px"></div>
      </div>

      <div style="margin-top:12px;display:flex;gap:8px;align-items:center">
        <label class="muted-small">Qty</label>
        <div style="display:flex;gap:8px;align-items:center">
          <button class="btn ghost" id="qtyMinus">-</button>
          <div id="qtyVal" style="min-width:36px;text-align:center;font-weight:800">1</div>
          <button class="btn ghost" id="qtyPlus">+</button>
        </div>
      </div>

      <div style="margin-top:16px;display:flex;gap:10px">
        <button class="btn" id="modalAdd">Add to cart</button>
        <button class="btn ghost" id="modalClose">Close</button>
      </div>
    </div>
  </div>
</div>

<!-- Checkout Modal (mock) -->
<div id="checkoutBackdrop" class="modal-backdrop" style="display:none">
  <div class="modal" style="max-width:720px;grid-template-columns:1fr">
    <h3>Checkout (Demo)</h3>
    <form id="checkoutForm" style="display:grid;gap:8px">
      <input name="name" placeholder="Full name" required style="padding:10px;border-radius:8px;border:1px solid rgba(15,23,36,0.06)">
      <input name="email" placeholder="Email" required type="email" style="padding:10px;border-radius:8px;border:1px solid rgba(15,23,36,0.06)">
      <input name="address" placeholder="Shipping address" required style="padding:10px;border-radius:8px;border:1px solid rgba(15,23,36,0.06)">
      <div style="display:flex;gap:8px;justify-content:flex-end">
        <button class="btn" type="submit">Place order (Demo)</button>
        <button class="btn ghost" type="button" id="checkoutCancel">Cancel</button>
      </div>
    </form>
  </div>
</div>

<script>
/* =========================
   Product data (sample)
   Add images, descriptions as needed
   Each product has images[], sizes[], colors[] (colors are names)
   ========================= */
const PRODUCTS = [
  { id: 'p1', title: 'Signature Hoodie', category: 'hoodies', price: 65,
    images: [
      'https://source.unsplash.com/collection/190727/800x800?sig=1',
      'https://source.unsplash.com/collection/190727/800x800?sig=2',
      'https://source.unsplash.com/collection/190727/800x800?sig=3'
    ],
    desc: 'Cozy fleece with structured hood and soft interior. Tapered fit.',
    sizes: ['S','M','L','XL'],
    colors: ['Black','Charcoal','Olive']
  },
  { id: 'p2', title: 'Tech Sweatpants', category: 'sweatpants', price: 58,
    images: [
      'https://source.unsplash.com/featured/?sweatpants,athlete',
      'https://source.unsplash.com/featured/?joggers,fitness'
    ],
    desc: 'Moisture-wicking, four-way stretch. Zip pockets and tapered ankle.',
    sizes: ['S','M','L','XL'],
    colors: ['Black','Navy']
  },
  { id: 'p3', title: 'Performance Shirt', category: 'shirts', price: 28,
    images: [
      'https://source.unsplash.com/featured/?tshirt,athlete',
      'https://source.unsplash.com/featured/?training,tee'
    ],
    desc: 'Lightweight training tee with anti-odor technology.',
    sizes: ['S','M','L','XL'],
    colors: ['White','Black','Grey']
  },
  { id: 'p4', title: 'CL Runner Shoes', category: 'shoes', price: 120,
    images: [
      'https://source.unsplash.com/featured/?sneakers,trainers',
      'https://source.unsplash.com/featured/?running-shoes'
    ],
    desc: 'Responsive midsole, breathable upper, ideal for daily runs.',
    sizes: ['8','9','10','11','12'],
    colors: ['Black','White']
  },
  { id: 'p5', title: 'Zip Sweatshirt', category: 'sweatshirts', price: 72,
    images: [
      'https://source.unsplash.com/featured/?zipper,sweatshirt'
    ],
    desc: 'Full zip with ergonomic seams and secure pockets.',
    sizes: ['S','M','L','XL'],
    colors: ['Black','Heather']
  },
  { id: 'p6', title: 'Comfy Jogger', category: 'sweatpants', price: 49,
    images: [
      'https://source.unsplash.com/featured/?joggers'
    ],
    desc: 'Relaxed fit with elastic cuffs; great for lounge & travel.',
    sizes: ['S','M','L','XL'],
    colors: ['Grey','Navy']
  }
];

/* =========================
   State & UI elements
   ========================= */
let filtered = [...PRODUCTS];
let CART = JSON.parse(localStorage.getItem('cl_cart') || '[]');

const productGrid = document.getElementById('productGrid');
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearch');
const categoryFilters = document.getElementById('categoryFilters');
const sortSel = document.getElementById('sortSel');

const cartToggle = document.getElementById('cartToggle');
const cartDrawer = document.getElementById('cartDrawer');
const cartCountEl = document.getElementById('cartCount');
const cartItemsEl = document.getElementById('cartItems');
const cartTotalEl = document.getElementById('cartTotal');

const modalBackdrop = document.getElementById('modalBackdrop');
const modalTitle = document.getElementById('modalTitle');
const modalPrice = document.getElementById('modalPrice');
const modalCategory = document.getElementById('modalCategory');
const modalDesc = document.getElementById('modalDesc');
const modalMainImg = document.getElementById('modalMainImg');
const modalThumbs = document.getElementById('modalThumbs');
const sizeOptions = document.getElementById('sizeOptions');
const colorOptions = document.getElementById('colorOptions');
const qtyVal = document.getElementById('qtyVal');
const qtyMinus = document.getElementById('qtyMinus');
const qtyPlus = document.getElementById('qtyPlus');
const modalAdd = document.getElementById('modalAdd');
const modalClose = document.getElementById('modalClose');

const modalBackdropEl = document.getElementById('modalBackdrop');

const checkoutBackdrop = document.getElementById('checkoutBackdrop');
const checkoutForm = document.getElementById('checkoutForm');
const checkoutBtn = document.getElementById('checkoutBtn');
const checkoutCancel = document.getElementById('checkoutCancel');

/* =========================
   Utilities
   ========================= */
function saveCart(){ localStorage.setItem('cl_cart', JSON.stringify(CART)); updateCartUI(); }
function formatPrice(n){ return '$' + n.toFixed(2); }

/* =========================
   Render products
   ========================= */
function renderProducts(list){
  productGrid.innerHTML = '';
  if(list.length === 0){
    productGrid.innerHTML = '<div class="muted">No products found.</div>';
    return;
  }
  list.forEach(p=>{
    const el = document.createElement('div');
    el.className = 'card';
    el.innerHTML = `
      <div class="img"><img src="${p.images[0]}" alt="${p.title}"></div>
      <div class="meta">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-weight:800">${p.title}</div>
            <div class="muted" style="margin-top:6px">${p.category}</div>
          </div>
          <div style="text-align:right">
            <div class="price">${formatPrice(p.price)}</div>
            <div class="muted" style="font-size:12px">USD</div>
          </div>
        </div>
        <div style="display:flex;gap:8px;margin-top:12px">
          <button class="btn" onclick="openProduct('${p.id}')">View</button>
          <button class="btn ghost" onclick="quickAdd('${p.id}')">Quick add</button>
        </div>
      </div>
    `;
    productGrid.appendChild(el);
  });
}
renderProducts(PRODUCTS);

/* =========================
   Search & filter & sort
   ========================= */
function applyFilters(){
  const q = searchInput.value.trim().toLowerCase();
  const activeCat = [...categoryFilters.querySelectorAll('.pill.selected')].map(n=>n.dataset.cat)[0] || 'all';
  filtered = PRODUCTS.filter(p=>{
    if(activeCat !== 'all' && p.category !== activeCat) return false;
    if(!q) return true;
    const hay = (p.title + ' ' + p.desc + ' ' + p.category).toLowerCase();
    return hay.includes(q);
  });

  const sort = sortSel.value;
  if(sort === 'price-asc') filtered.sort((a,b)=>a.price-b.price);
  else if(sort === 'price-desc') filtered.sort((a,b)=>b.price-a.price);
  else if(sort === 'alpha') filtered.sort((a,b)=>a.title.localeCompare(b.title));
  // featured default keep original order
  renderProducts(filtered);
}

/* search */
searchInput.addEventListener('input', ()=>{ applyFilters(); });
clearSearchBtn.addEventListener('click', ()=>{ searchInput.value=''; applyFilters(); });

/* categories */
categoryFilters.addEventListener('click', e=>{
  const pill = e.target.closest('.pill');
  if(!pill) return;
  [...categoryFilters.querySelectorAll('.pill')].forEach(p=>p.classList.remove('selected'));
  pill.classList.add('selected');
  applyFilters();
});
/* set All selected by default */
categoryFilters.querySelector('.pill[data-cat="all"]').classList.add('selected');

/* sort */
sortSel.addEventListener('change', applyFilters);

/* =========================
   Modal: product detail
   ========================= */
let modalState = { productId:null, qty:1, size:null, color:null, selectedImgIndex:0 };

function openProduct(id){
  const p = PRODUCTS.find(x=>x.id===id);
  if(!p) return;
  modalState.productId = id;
  modalState.qty = 1;
  modalState.size = p.sizes?.[0] || null;
  modalState.color = p.colors?.[0] || null;
  modalState.selectedImgIndex = 0;

  modalTitle.textContent = p.title;
  modalPrice.textContent = formatPrice(p.price);
  modalCategory.textContent = p.category;
  modalDesc.textContent = p.desc;
  modalMainImg.src = p.images[0];

  // thumbs
  modalThumbs.innerHTML = '';
  p.images.forEach((src, i)=>{
    const t = document.createElement('img');
    t.src = src;
    if(i===0) t.classList.add('active');
    t.addEventListener('click', ()=>{ modalMainImg.src = src; modalThumbs.querySelectorAll('img').forEach(x=>x.classList.remove('active')); t.classList.add('active'); modalState.selectedImgIndex = i; });
    modalThumbs.appendChild(t);
  });

  // sizes
  sizeOptions.innerHTML = '';
  (p.sizes || []).forEach(s=>{
    const btn = document.createElement('div');
    btn.className='pill';
    btn.textContent=s;
    if(s === modalState.size) btn.classList.add('selected');
    btn.style.cursor='pointer';
    btn.addEventListener('click', ()=>{ modalState.size = s; sizeOptions.querySelectorAll('.pill').forEach(x=>x.classList.remove('selected')); btn.classList.add('selected'); });
    sizeOptions.appendChild(btn);
  });

  // colors
  colorOptions.innerHTML = '';
  (p.colors || []).forEach(c=>{
    const btn = document.createElement('div');
    btn.className='pill';
    btn.textContent=c;
    if(c === modalState.color) btn.classList.add('selected');
    btn.style.cursor='pointer';
    btn.addEventListener('click', ()=>{ modalState.color = c; colorOptions.querySelectorAll('.pill').forEach(x=>x.classList.remove('selected')); btn.classList.add('selected'); });
    colorOptions.appendChild(btn);
  });

  // qty
  qtyVal.textContent = modalState.qty;
  modalBackdrop.style.display = 'grid';
  modalBackdrop.focus?.();
}

/* modal qty controls */
qtyMinus.addEventListener('click', ()=>{ if(modalState.qty>1) modalState.qty--; qtyVal.textContent = modalState.qty; });
qtyPlus.addEventListener('click', ()=>{ modalState.qty++; qtyVal.textContent = modalState.qty; });
modalClose.addEventListener('click', closeModal);
modalBackdrop.addEventListener('click', (e)=>{ if(e.target === modalBackdrop) closeModal(); });

/* add to cart from modal */
modalAdd.addEventListener('click', ()=>{
  if(!modalState.productId) return;
  const id = modalState.productId;
  const optionKey = `${id}::${modalState.size || 'noSize'}::${modalState.color || 'noColor'}`;
  const existing = CART.find(i => i.key === optionKey);
  if(existing) existing.qty += modalState.qty;
  else {
    CART.push({
      key: optionKey,
      productId: id,
      qty: modalState.qty,
      size: modalState.size,
      color: modalState.color
    });
  }
  saveCart();
  closeModal();
  openCart();
});

function closeModal(){
  modalBackdrop.style.display = 'none';
  modalState = { productId:null, qty:1, size:null, color:null, selectedImgIndex:0 };
}

/* =========================
   Quick add (no options) - just adds base variant
   ========================= */
function quickAdd(id){
  const baseKey = `${id}::${(PRODUCTS.find(p=>p.id===id).sizes?.[0]||'noSize')}::${(PRODUCTS.find(p=>p.id===id).colors?.[0]||'noColor')}`;
  const existing = CART.find(i=>i.key === baseKey);
  if(existing) existing.qty += 1;
  else CART.push({ key: baseKey, productId: id, qty: 1, size: PRODUCTS.find(p=>p.id===id).sizes?.[0]||null, color: PRODUCTS.find(p=>p.id===id).colors?.[0]||null});
  saveCart();
  openCart();
}

/* =========================
   Cart UI
   ========================= */
function updateCartUI(){
  const count = CART.reduce((s,i)=>s+i.qty,0);
  cartCountEl.style.display = count ? 'grid' : 'none';
  cartCountEl.textContent = count;
  cartItemsEl.innerHTML = '';
  let subtotal = 0;
  CART.forEach(item=>{
    const p = PRODUCTS.find(pp => pp.id === item.productId);
    const lineTotal = p.price * item.qty;
    subtotal += lineTotal;
    const div = document.createElement('div');
    div.className = 'cart-item';
    div.innerHTML = `
      <img src="${p.images[0]}" alt="${p.title}">
      <div class="info">
        <div style="font-weight:700">${p.title}</div>
        <div class="muted" style="font-size:13px">${item.size? item.size + ' • ' : ''}${item.color? item.color : ''}</div>
        <div style="margin-top:8px;font-weight:800">${formatPrice(lineTotal)}</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:center">
        <button class="btn ghost" onclick="changeQty('${item.key}',1)">+</button>
        <div style="font-weight:800">${item.qty}</div>
        <button class="btn ghost" onclick="changeQty('${item.key}',-1)">-</button>
        <button class="btn ghost" style="margin-top:6px" onclick="removeItem('${item.key}')">Remove</button>
      </div>
    `;
    cartItemsEl.appendChild(div);
  });
  cartTotalEl.textContent = formatPrice(subtotal);
}

function changeQty(key, delta){
  const idx = CART.findIndex(i=>i.key===key);
  if(idx === -1) return;
  CART[idx].qty += delta;
  if(CART[idx].qty <= 0) CART.splice(idx,1);
  saveCart();
}

function removeItem(key){
  CART = CART.filter(i => i.key !== key);
  saveCart();
}

/* open/close cart drawer */
function openCart(){ cartDrawer.classList.toggle('open'); cartDrawer.setAttribute('aria-hidden', !cartDrawer.classList.contains('open')); updateCartUI(); }
document.getElementById('cartToggle').addEventListener('click', openCart);
document.getElementById('clearCartBtn').addEventListener('click', ()=>{ CART = []; saveCart(); });
document.getElementById('checkoutBtn').addEventListener('click', ()=>{ if(CART.length === 0){ alert('Your cart is empty.'); return; } openCheckout(); });

/* save cart and update UI init */
saveCart();

/* =========================
   Checkout (mock)
   ========================= */
function openCheckout(){
  checkoutBackdrop.style.display = 'grid';
}
checkoutCancel.addEventListener('click', ()=>{ checkoutBackdrop.style.display = 'none'; });
checkoutForm.addEventListener('submit', (e)=>{
  e.preventDefault();
  // mock order payload
  const payload = {
    name: checkoutForm.name.value,
    email: checkoutForm.email.value,
    address: checkoutForm.address.value,
    items: CART
  };
  console.log('ORDER (demo):', payload);
  alert('Order placed (demo). Check console for payload. Implement server + payment for production.');
  CART = []; saveCart();
  checkoutBackdrop.style.display = 'none';
  cartDrawer.classList.remove('open');
});

/* =========================
   Persist product search on Enter
   ========================= */
searchInput.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') applyFilters(); });

/* =========================
   Init default state
   ========================= */
applyFilters();
updateCartUI();

/* Close backdrops with Escape */
document.addEventListener('keydown', (e)=>{
  if(e.key === 'Escape'){
    if(modalBackdrop.style.display === 'grid') closeModal();
    if(checkoutBackdrop.style.display === 'grid') checkoutBackdrop.style.display = 'none';
    if(cartDrawer.classList.contains('open')){ cartDrawer.classList.remove('open'); cartDrawer.setAttribute('aria-hidden','true'); }
  }
});
</script>
</body>
</html>
