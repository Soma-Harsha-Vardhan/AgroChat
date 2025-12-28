# knowledge_base.py
# ============================================================
# Structured agricultural knowledge dictionary (single file).
# ============================================================

KNOWLEDGE = {
    "Diseases": {
        "Pepper Bell Bacterial Spot": {
            "Symptoms": "Small dark water-soaked spots on leaves and fruits, yellow halos, leaf drop.",
            "Cause": "Xanthomonas bacteria.",
            "Organic Control": "Neem oil (5 ml/L), copper spray (2 g/L).",
            "Chemical Control": "Copper oxychloride (3 g/L), streptomycin sprays.",
            "Prevention": "Disease-free seeds, crop rotation, avoid overhead watering.",
            "Fertilizer Recommendation": "Balanced NPK 10-10-10.",
            "Climate Conditions": "High humidity, warm temperature (25–30°C).",
            "Confusion With": "Magnesium deficiency, sunscald."
        },

        "Pepper Bell Healthy": {
            "Condition": "Normal deep-green leaves, strong stems.",
            "Fertilizer Recommendation": "NPK 12-12-17 every 25 days.",
            "Prevention": "Proper irrigation, balanced fertilizer."
        },

        "Potato Early Blight": {
            "Symptoms": "Brown concentric rings on lower leaves, yellowing.",
            "Cause": "Alternaria solani.",
            "Organic Control": "Neem oil (3 ml/L).",
            "Chemical Control": "Mancozeb (2.5 g/L).",
            "Prevention": "Crop rotation, avoid overhead irrigation.",
            "Fertilizer Recommendation": "NPK 5-10-20."
        },

        "Potato Late Blight": {
            "Symptoms": "Dark greasy lesions, white mold under leaves, tuber rot.",
            "Cause": "Phytophthora infestans.",
            "Organic Control": "Neem oil (4 ml/L), copper oxychloride (3 g/L).",
            "Chemical Control": "Mancozeb, Metalaxyl.",
            "Prevention": "Remove infected plants, avoid water stagnation.",
            "Climate Conditions": "Cool + humid weather."
        },

        "Potato Healthy": {
            "Condition": "Dark green leaves, strong stems.",
            "Prevention": "Adequate nitrogen, well-drained soil.",
            "Fertilizer Recommendation": "NPK 13-40-13 at planting → 20-20-20."
        },

        "Tomato Bacterial Spot": {
            "Symptoms": "Small dark leaf spots, scabby fruits.",
            "Cause": "Xanthomonas bacteria.",
            "Organic Control": "Neem oil, copper sprays.",
            "Chemical Control": "Copper fungicides.",
            "Prevention": "Avoid overhead watering.",
            "Fertilizer Recommendation": "NPK 5-10-10."
        },

        "Tomato Early Blight": {
            "Symptoms": "Concentric brown rings, leaf yellowing.",
            "Cause": "Alternaria solani.",
            "Organic Control": "Compost tea, neem oil.",
            "Chemical Control": "Mancozeb, chlorothalonil.",
            "Prevention": "Remove infected leaves.",
            "Fertilizer Recommendation": "NPK 10-20-20."
        },

        "Tomato Late Blight": {
            "Symptoms": "Greasy lesions, white mold under leaves.",
            "Cause": "Phytophthora infestans.",
            "Organic Control": "Neem, copper oxychloride.",
            "Chemical Control": "Mancozeb, Metalaxyl.",
            "Prevention": "Remove infected plants.",
            "Fertilizer Recommendation": "Increase potassium."
        },

        "Tomato Leaf Mold": {
            "Symptoms": "Yellow patches on top of leaf, olive mold underside.",
            "Cause": "Passalora fulva.",
            "Organic Control": "Pruning, ventilation, neem spray.",
            "Chemical Control": "Copper or chlorothalonil fungicides.",
            "Prevention": "Reduce humidity."
        },

        "Tomato Septoria Leaf Spot": {
            "Symptoms": "Numerous small brown spots with pale centers.",
            "Cause": "Septoria lycopersici.",
            "Organic Control": "Neem spray.",
            "Chemical Control": "Copper fungicide.",
            "Prevention": "Avoid overhead watering."
        },

        "Tomato Spider Mites": {
            "Symptoms": "Leaf bronzing, tiny webs, yellow speckles.",
            "Cause": "Mites.",
            "Organic Control": "Neem oil (2 ml/L), soap spray.",
            "Prevention": "Increase humidity."
        },

        "Tomato Target Spot": {
            "Symptoms": "Circular spots with rings.",
            "Cause": "Corynespora cassiicola.",
            "Organic Control": "Neem, sanitation.",
            "Chemical Control": "Fungicides.",
            "Prevention": "Good airflow."
        },

        "Tomato Mosaic Virus": {
            "Symptoms": "Mottled leaves, twisted shape.",
            "Cause": "Tomato mosaic virus.",
            "Organic Control": "Remove infected plants.",
            "Prevention": "Sanitize tools."
        },

        "Tomato Yellow Leaf Curl Virus": {
            "Symptoms": "Yellow curled leaves, stunting.",
            "Cause": "Whitefly-transmitted virus.",
            "Organic Control": "Sticky traps, neem oil.",
            "Prevention": "Remove infected plants."
        },

        "Tomato Healthy": {
            "Condition": "Healthy green leaves, no visible spots, good vigor.",
            "Prevention": "Proper irrigation, balanced fertilizer, good spacing.",
            "Fertilizer Recommendation": "NPK 12-12-36 during fruiting stage.",
            "Climate Conditions": "Warm, moderate humidity."
        }
    },

    "Deficiencies": {
        "Nitrogen Deficiency": {
            "Symptoms": "Pale yellow older leaves.",
            "Fix": "Compost, cow manure, urea (1 tsp/L).",
            "Prevention": "Regular compost application."
        },
        "Phosphorus Deficiency": {
            "Symptoms": "Purplish leaves, slow growth.",
            "Fix": "DAP, bone meal.",
            "Prevention": "Maintain soil pH 6–7."
        },
        "Potassium Deficiency": {
            "Symptoms": "Brown leaf edges (scorching).",
            "Fix": "MOP fertilizer.",
            "Prevention": "Balanced NPK schedule."
        },
        "Calcium Deficiency": {
            "Symptoms": "Blossom end rot.",
            "Fix": "Calcium nitrate (1 tsp/L).",
            "Prevention": "Avoid irregular watering."
        },
        "Magnesium Deficiency": {
            "Symptoms": "Yellowing between veins on older leaves.",
            "Fix": "Epsom salt spray (1 tsp/L).",
            "Prevention": "Maintain soil pH 6–7."
        },
        "Iron Deficiency": {
            "Symptoms": "Yellowing between veins on young leaves.",
            "Fix": "Ferrous sulfate spray.",
            "Prevention": "Avoid alkaline soil."
        }
    },

    "Pests": {
        "Aphids": {
            "Symptoms": "Sticky leaves (honeydew), curling.",
            "Organic Control": "Neem oil (2 ml/L), soap spray.",
            "Chemical Control": "Imidacloprid."
        },
        "Whiteflies": {
            "Symptoms": "Tiny white insects flying when disturbed.",
            "Organic Control": "Yellow sticky traps.",
            "Chemical Control": "Thiamethoxam."
        },
        "Thrips": {
            "Symptoms": "Silver streaks, leaf distortion.",
            "Control": "Spinosad, neem spray."
        },
        "Mealybugs": {
            "Symptoms": "Cotton-like clusters.",
            "Organic Control": "Spirit + soap spray."
        },
        "Fruit Worms": {
            "Symptoms": "Holes in fruits.",
            "Control": "Bt spray (Bacillus thuringiensis)."
        }
    },

    "Stages": {
        "Seedling": {
            "Fertilizer": "NPK 19-19-19 (half dose).",
            "Care": "Avoid overwatering."
        },
        "Vegetative": {
            "Fertilizer": "NPK 20-20-20.",
            "Care": "Watch for fungal infections."
        },
        "Flowering": {
            "Fertilizer": "NPK 15-30-15.",
            "Care": "Maintain calcium."
        },
        "Fruiting": {
            "Fertilizer": "NPK 12-12-17 or 14-14-21.",
            "Care": "Monitor pests."
        }
    },

    "Climate": {
        "High Humidity": {
            "Risk": "Leaf mold, late blight.",
            "Advice": "Improve ventilation."
        },
        "Hot Dry": {
            "Risk": "Spider mites.",
            "Advice": "Increase humidity."
        },
        "Cool Wet": {
            "Risk": "Late blight.",
            "Advice": "Use protective fungicide spray."
        }
    },

    "Dosages": {
        "Neem Oil": "2–5 ml per liter.",
        "Copper Oxychloride": "2–3 g per liter.",
        "Mancozeb": "2–2.5 g per liter.",
        "Metalaxyl": "Use as per label.",
        "Imidacloprid": "0.3 ml per liter.",
        "Epsom Salt": "1 tsp per liter.",
        "Calcium Nitrate": "1 tsp per liter."
    }
}

print("✅ Knowledge dictionary created. Diseases:", len(KNOWLEDGE["Diseases"]))
