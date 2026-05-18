# =========================================================
# BUSINESS SALES ANALYTICS DASHBOARD
# FULL PYTHON CODE
# =========================================================

# Install Required Libraries:
# pip install pandas matplotlib pillow

# =========================================================
# IMPORT LIBRARIES
# =========================================================

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# =========================================================
# CREATE SALES TREND CHART
# =========================================================

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 18000, 17000, 22000, 25000]

plt.figure(figsize=(5,3))

plt.plot(months, sales, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

sales_chart = "sales_trend.png"

plt.savefig(sales_chart, bbox_inches='tight')

plt.close()

# =========================================================
# CREATE CATEGORY PROFIT CHART
# =========================================================

categories = ["Technology", "Furniture", "Office Supplies"]

profits = [18000, 7000, 12000]

plt.figure(figsize=(5,3))

plt.bar(categories, profits)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

category_chart = "category_profit.png"

plt.savefig(category_chart, bbox_inches='tight')

plt.close()

# =========================================================
# CREATE REGIONAL SALES PIE CHART
# =========================================================

regions = ["West", "East", "South", "Central"]

region_sales = [42000, 30000, 18000, 25000]

plt.figure(figsize=(5,3))

plt.pie(
    region_sales,
    labels=regions,
    autopct='%1.1f%%'
)

plt.title("Regional Sales Distribution")

region_chart = "region_sales.png"

plt.savefig(region_chart, bbox_inches='tight')

plt.close()

# =========================================================
# CREATE DASHBOARD BACKGROUND
# =========================================================

img = Image.new(
    "RGB",
    (1400, 900),
    color=(240, 240, 245)
)

draw = ImageDraw.Draw(img)

# =========================================================
# LOAD FONTS
# =========================================================

try:
    title_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        36
    )

    heading_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        22
    )

    text_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        18
    )

except:
    title_font = ImageFont.load_default()
    heading_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# =========================================================
# HEADER SECTION
# =========================================================

draw.rectangle(
    [0, 0, 1400, 100],
    fill=(30, 60, 120)
)

draw.text(
    (320, 30),
    "Business Sales Analytics Dashboard",
    fill="white",
    font=title_font
)

# =========================================================
# KPI CARDS
# =========================================================

kpis = [
    ("Total Sales", "$120K"),
    ("Total Profit", "$25K"),
    ("Total Orders", "560"),
    ("Profit Margin", "20%")
]

x = 40

for title, value in kpis:

    draw.rounded_rectangle(
        [x, 140, x+300, 250],
        radius=15,
        fill="white"
    )

    draw.text(
        (x+20, 170),
        title,
        fill="black",
        font=heading_font
    )

    draw.text(
        (x+20, 210),
        value,
        fill=(20, 100, 20),
        font=heading_font
    )

    x += 340

# =========================================================
# INSERT CHARTS
# =========================================================

sales_img = Image.open(sales_chart)

sales_img = sales_img.resize((420, 260))

img.paste(sales_img, (40, 320))

# ---------------------------------------------------------

category_img = Image.open(category_chart)

category_img = category_img.resize((420, 260))

img.paste(category_img, (490, 320))

# ---------------------------------------------------------

region_img = Image.open(region_chart)

region_img = region_img.resize((420, 260))

img.paste(region_img, (940, 320))

# =========================================================
# BUSINESS INSIGHTS SECTION
# =========================================================

draw.rounded_rectangle(
    [40, 620, 1360, 860],
    radius=20,
    fill="white"
)

draw.text(
    (60, 650),
    "Business Insights & Recommendations",
    fill="black",
    font=title_font
)

insights = [

    "• Technology category generated the highest profit.",

    "• West region achieved maximum sales performance.",

    "• Sales increased significantly during Q4 season.",

    "• Furniture category has lower profit margins.",

    "• Increase inventory before holiday sales periods.",

    "• Improve marketing in low-performing regions.",

    "• Reduce discounts on low-profit products."
]

y = 720

for item in insights:

    draw.text(
        (80, y),
        item,
        fill="black",
        font=text_font
    )

    y += 45

# =========================================================
# FOOTER SECTION
# =========================================================

draw.rectangle(
    [0, 870, 1400, 900],
    fill=(30, 60, 120)
)

draw.text(
    (420, 875),
    "Created using Python, Pandas, Plotly & Streamlit",
    fill="white",
    font=text_font
)

# =========================================================
# SAVE FINAL DASHBOARD
# =========================================================

dashboard_file = "business_sales_dashboard.png"

img.save(dashboard_file)

print("Dashboard Created Successfully!")

print("Saved File:", dashboard_file)