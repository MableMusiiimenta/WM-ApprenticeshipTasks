name = "   "
name.strip()
""

Mario Wolf
11:17 AM
name = "   Filter   "
"Filter"

Mario Wolf
11:19 AM
product_id
↓
retrieve existing product
↓
show current values
↓
user changes values
↓
receive submitted values
↓
convert
↓
validate
↓
update existing product
↓
redirect back to product
no existing product
→ INSERT
→ new ID

Mario Wolf
11:20 AM
existing product ID
→ UPDATE that row
→ same ID
/products/<product_id>/edit
@app.route(
    "/products/<int:product_id>/edit",
    methods=["GET", "POST"]
)

Mario Wolf
11:21 AM
product_id
↓
get_product(product_id)
↓
does it exist?
   ↓
yes → show edit form
no  → 404
POST
submitted changes
↓
convert
↓
validate
↓
update product
↓
redirect to /products/<id>

Mario Wolf
11:23 AM
UPDATE products
SET
    name = ?,
    price = ?,
    stock = ?,
    active = ?
WHERE id = ?

Mario Wolf
11:25 AM
<input
    type="text"
    name="name"
    value="{{ product['name'] }}"
>
<input
    type="checkbox"
    name="active"
    {% if product["active"] %}checked{% endif %}
>