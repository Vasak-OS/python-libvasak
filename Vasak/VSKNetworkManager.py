import gi
gi.require_version("NM", "1.0")
from gi.repository import NM

class VSKNetworkManager:
    def __init__(self):
        self.__client = NM.Client.new(None)
        pass

    def get_active_connections(self):
        active_connections = self.__client.get_active_connections()
        return active_connections

    @staticmethod
    def get_connection_type(connection):
        connection_type = "UNKNOWN"
        conn_type = connection.get_connection_type()
        if 'ethernet' in conn_type:
            connection_type = "ETHERNET"
        elif 'wireless' in conn_type:
            connection_type = "WIRELESS"
        return connection_type

if __name__ == "__main__":
    nm = VSKNetworkManager()
    print(nm.get_active_connections()[0].get_id())
    print(nm.get_active_connections()[0].get_state())
    print(nm.get_active_connections()[0].get_default())
    print(nm.get_active_connections()[0].get_devices())
    print(nm.get_active_connections()[0].get_connection())
    print(nm.get_active_connections()[0].get_connection().get_id())
    print(nm.get_active_connections()[0].get_connection().get_uuid())
    print(nm.get_active_connections()[0].get_connection().get_connection_type())
    connection = nm.get_active_connections()[0].get_connection()
    print(nm.get_connection_type(connection))
