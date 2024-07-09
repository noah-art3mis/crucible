import yaml
from utils.my_types import Report


def save_logs(outputs: Report, run_id: str):
    with open(f"outputs/{run_id}.yaml", "w", encoding="utf-8") as f:
        yaml.dump(outputs.header, f, indent=2, allow_unicode=True, sort_keys=False)
        yaml.dump(outputs.results, f, indent=2, allow_unicode=True, sort_keys=False)
