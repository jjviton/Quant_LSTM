import schedule
import time
import subprocess

def run_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script {script_path}: {e}")

def schedule_scripts():
    # Programa tus scripts aquí
    # Ejemplo: ejecutar un script todos los días a las 10:00 AM
    schedule.every().day.at("19:07").do(run_script, script_path="C:\\Users\\jjjimenez\\Documents\\J3\\100.- cursos\\Quant_udemy\\programas\\Projects\\997_scheduler_J\\997_scheduler_J\\beeper.py")

    # Ejemplo: ejecutar un script cada hora
    # schedule.every().hour.do(run_script, script_path="beeper.py")
    schedule.every().minute.do(run_script,script_path="C:\\Users\\jjjimenez\\Documents\\J3\\100.- cursos\\Quant_udemy\\programas\\Projects\\997_scheduler_J\\997_scheduler_J\\beeper.py" )

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_scripts()
