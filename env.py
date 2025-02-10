import os

os.environ.setdefault(
    "DATABASE_URL",
    (
        (
            (
                "postgresql://neondb_owner:npg_GDQHjxw97AnS@ep-soft-wildflower"
                "-a2o1ouzz.eu-central-1.aws.neon.tech/"
                "pluck_curve_yelp_979423"
            )
        )
    )
)

os.environ.setdefault(
    "SECRET_KEY",
    "pontypridd1989"
)

os.environ.setdefault(
        "CLOUDINARY_URL",
        (
            "cloudinary://445662134364256:ljP2vryq5Um1BIy8CCn6lGe6iTY"
            "@dgkiu4va5?secure=true"
        )
    )
