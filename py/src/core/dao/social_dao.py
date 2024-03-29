import cx_Oracle
from core.config import ConfigLoader

class SocialDAO:
    def get_messages(this,room:int) -> list[tuple[str, int, cx_Oracle.Timestamp, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM UZENET WHERE KOZOSSEG = :1 ORDER BY IDOPONT",[room])
            db_data: list[tuple[str, int, cx_Oracle.Timestamp, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for u_name, r_room, date, content in db_data:
                result.append((u_name, r_room, date, content))

            return result
        except Exception as e:
            print(e)
        return list()

    def get_room(this, u_name) -> list[tuple[int, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM KOZOSSEG WHERE KOZOSSEG.ID != 0 and KOZOSSEG.ID in (Select KOZOSSEG from KOZOSSEGTAGJA where FELHASZNALONEV = :1)", [u_name])
            db_data: list[tuple[int, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()
            for room_id, room_name in db_data:
                result.append((room_id, room_name))
            return result
        except Exception as e:
            print(e)
        return list()

    def insert_to_room(this, uname, room_id) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT into kozossegtagja values (:1, :2)", [uname, room_id])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def make_room(this, r_id, r_name) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT into kozosseg values (:1, :2)", [r_id, r_name])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def get_room_id(this)->int:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT max(ID)+1 FROM KOZOSSEG")
            db_data: list[tuple[int, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()
            for room_id in db_data:
                result.append((room_id))
            return result[0][0]
        except Exception as e:
            print(e)
        return -1

    def get_non_member_room(this, u_name) -> list[tuple[int, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM KOZOSSEG WHERE KOZOSSEG.ID != 0 and KOZOSSEG.ID not in (Select KOZOSSEG from KOZOSSEGTAGJA where FELHASZNALONEV = :1)", [u_name])
            db_data: list[tuple[int, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()
            for room_id, room_name in db_data:
                result.append((room_id, room_name))
            return result
        except Exception as e:
            print(e)
        return list()

    def get_forum_messages(this) -> list[tuple[str, int, cx_Oracle.Timestamp, str]]:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM UZENET WHERE KOZOSSEG = 0 order by IDOPONT")
            db_data: list[tuple[str, int, cx_Oracle.Timestamp, str]] = cursor.fetchall()
            ConfigLoader.get_connection_pool().release(connection)
            result = list()

            for u_name, r_room, date, content in db_data:
                result.append((u_name, r_room, date, content))

            return result
        except Exception as e:
            print(e)
        return list()

    def delete_forum_msg(this, uname, date) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM UZENET WHERE KULDO = :1 AND IDOPONT = :2", [uname, date])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False

    def update_msg(this, uname, time, new) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("UPDATE UZENET SET SZOVEG = :1 WHERE KULDO = :2 AND IDOPONT = :3", [new, uname, time])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False


    def send_message(this, u_name, room_id, content) -> bool:
        try:
            connection = ConfigLoader.get_connection_pool().acquire()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO UZENET(KULDO, KOZOSSEG, IDOPONT, SZOVEG) VALUES (:1, :2, current_timestamp, :3)", [u_name, room_id, content])
            connection.commit()
            ConfigLoader.get_connection_pool().release(connection)
            return True

        except Exception as e:
            print(e)
            return False