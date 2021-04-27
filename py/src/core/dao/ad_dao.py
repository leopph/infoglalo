import cx_Oracle
from src.core.config import ConfigLoader
from tkinter import PhotoImage


class AdDAO:
    def output_type_handler(this, cursor, name, default_type, size, precision, scale):
        if default_type == cx_Oracle.DB_TYPE_BLOB:
            return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)


    def find_all(this) -> list[tuple[str, str, PhotoImage]]:
        try:
            with cx_Oracle.connect(ConfigLoader.get_db_user(), ConfigLoader.get_db_pwd(), ConfigLoader.get_db_url(), encoding=ConfigLoader.get_db_encoding()) as connection:
                connection.outputtypehandler = this.output_type_handler
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM HIRDETES")

                db_data : list[tuple[int, str, str, str]] = cursor.fetchall()
                ret = list()

                for db_id, title, text, image in db_data:
                    ret.append((title, text, PhotoImage(data = image)))
                return ret


        except Exception as e:
            print(e)

        return list()