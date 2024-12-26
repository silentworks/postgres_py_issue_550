import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")

supabase = create_client(url, key)


def main():
    query = supabase.table("cities").select("id, name").eq("country_id", 1)
    q1 = query.in_("id", ["1", "3"]).execute()
    q2 = query.in_("id", ["2", "4"]).execute()

    print(f"querying: {q1.data} and {q2.data}")


if __name__ == "__main__":
    main()
