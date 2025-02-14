import os 
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent / "dbt" 
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH)) 

profile_config = ProfileConfig(
    profile_name="dbt_data_pipeline",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn_id",
        profile_args={"database": "dbt_airflow_db",
                        "schema": "dbt_airflow_schema"
                        }
    )
)

dbt_snowflake_dag = DbtDag(
     project_config=ProjectConfig( 
         DBT_ROOT_PATH / "dbt_data_pipeline", 
     ), 
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2024, 10, 17),
    catchup=False,
    dag_id="dbt_dag"
    )    