import yaml


def save_logs(outputs, run_id):
    with open(f"outputs/{run_id}.yaml", "w", encoding="utf-8") as f:
        yaml.dump(outputs, f, indent=2, allow_unicode=True, sort_keys=False)
