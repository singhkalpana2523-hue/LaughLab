import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import requests
from io import BytesIO

# ---------------- CONFIG ----------------
st.set_page_config(page_title="LaughLab – AI Meme & Poster Generator")

st.title("LaughLab – AI Meme & Poster Generator")
st.write("Create AI-powered memes and posters in seconds")

# ---------------- CAPTION LOGIC ----------------
def generate_caption(topic, mode):
    meme_captions = [
        f"When {topic} decides your fate 😂",
        f"Me vs {topic}. {topic} wins.",
        f"Nobody: Absolutely nobody: {topic}",
        f"That awkward moment when {topic} shows up"
    ]

    motivation_captions = [
        f"Believe in yourself, even when {topic} feels tough.",
        f"{topic} is hard, but giving up is harder.",
        f"Small steps today conquer {topic} tomorrow.",
        f"Your future self will thank you for facing {topic}."
    ]

    study_captions = [
        f"Focus on {topic}. Success will follow.",
        f"Master {topic} one concept at a time.",
        f"Consistency beats fear of {topic}.",
        f"{topic} is difficult until it becomes familiar."
    ]

    event_captions = [
        f"Join us for an exciting {topic}!",
        f"Don’t miss out on {topic}. See you there!",
        f"Get ready for {topic} – mark your calendar!",
        f"{topic}: Where ideas meet energy."
    ]

    if mode == "Meme":
        return random.choice(meme_captions)
    elif mode == "Motivational Poster":
        return random.choice(motivation_captions)
    elif mode == "Study Poster":
        return random.choice(study_captions)
    else:
        return random.choice(event_captions)

# ---------------- USER INPUT ----------------
topic = st.text_input("Enter a topic")

mode = st.selectbox(
    "Choose content type",
    ["Meme", "Motivational Poster", "Study Poster", "Event Poster"]
)

# ---------------- TEMPLATES ----------------
templates = {
    "Meme": {
        "Drake Hotline": "https://i.imgflip.com/30b1gx.jpg",
        "Distracted Boyfriend": "https://i.imgflip.com/1ur9b0.jpg",
    },
    "Motivational Poster": {
        "Sunrise": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "Mountain": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    },
    "Study Poster": {
        "Study Desk": "https://images.unsplash.com/photo-1513258496099-48168024aec0",
        "Library": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
    },
    "Event Poster": {
        "Stage Event": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30",
        "Conference": "https://images.unsplash.com/photo-1503428593586-e225b39bddfe",
    }
}

template_name = st.selectbox(
    "Choose a template",
    templates[mode].keys()
)

# ---------------- GENERATE OUTPUT ----------------
if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        caption = generate_caption(topic, mode)

        # Load image
        image_url = templates[mode][template_name]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content)).convert("RGB")

        draw = ImageDraw.Draw(img)

        # Load font
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        # Calculate text size
        bbox = draw.textbbox((0, 0), caption, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]


        # Position text
        x = (img.width - text_width) // 2
        if mode == "Meme":
            y = img.height - text_height - 30
        else:
            y = img.height // 2 - text_height // 2

        # Draw outline for readability
        for dx in [-2, -1, 1, 2]:
            for dy in [-2, -1, 1, 2]:
                draw.text((x + dx, y + dy), caption, font=font, fill="black")

        # Draw main text
        draw.text((x, y), caption, fill="white", font=font)

        # Show image
        st.image(img, width=450)

        # Download option
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        st.download_button(
            label="Download Image",
            data=buffer.getvalue(),
            file_name="laughlab_output.png",
            mime="image/png"
        )
