import diskinfo.diskinfo as DiskInfo
import json

class VSKDisks:
  def __init__(self):
    self.diskInfo = DiskInfo.DiskInfo()

  def getDisksList(self):
    jsondata = "["
    for disk in self.diskInfo.get_disk_list():
      print(disk)
      jsondata += self.diskToStringJSON(disk) + ","
    jsondata += "]"
    print(jsondata)
    return jsondata
  
  def diskToStringJSON(self, disk):
    datadisk = {
      "name": disk.get_name(),
      "deviceId": disk.get_device_id(),
      "model": disk.get_model(),
      "partition": {
        "type": disk.get_partition_table_type(),
        "list": self.partitionListToStringJSON(disk.get_partition_list()),
        "uuid": disk.get_partition_table_uuid()
      },
      "path": disk.get_path(),
      "serial": disk.get_serial_number(),
      "size": disk.get_size() * 512,
      "type": disk.get_type_str(),
    }
    return str(datadisk)
  
  def partitionListToStringJSON(self, partitionList):
    jsondata = "["
    for partition in partitionList:
      jsondata += self.partitionToStringJSON(partition) + ","
    jsondata += "]"
    return jsondata
  
  def partitionToStringJSON(self, partition):
    if partition.get_part_scheme() == "GPT":
      datapartition = {
        "path": partition.get_path(),
        "name": partition.get_name(),
        "size": partition.get_part_size() * 512,
        "offset": partition.get_part_offset() * 512,
        "type": partition.get_part_scheme(),
        "number": partition.get_part_number(),
        "deviceId": partition.get_part_device_id(),
        "fsVersion": partition.get_fs_version(),
        "fsUuid": partition.get_fs_uuid(),
        "fsUsage": partition.get_fs_usage(),
        "fsType": partition.get_fs_type(),
        "fsMountingPoint": partition.get_fs_mounting_point(),
        "fsLabel": partition.get_fs_label(),
        "fsFreeSize": partition.get_fs_free_size() * 512,
        "uuid": partition.get_part_uuid(),
        "label": partition.get_part_label(),
      }
    else:
      datapartition = {
        "path": partition.get_path(),
        "name": partition.get_name(),
        "size": partition.get_part_size() * 512,
        "offset": partition.get_part_offset() * 512,
        "type": partition.get_part_scheme(),
        "number": partition.get_part_number(),
        "deviceId": partition.get_part_device_id(),
        "fsVersion": partition.get_fs_version(),
        "fsUuid": partition.get_fs_uuid(),
        "fsUsage": partition.get_fs_usage(),
        "fsType": partition.get_fs_type(),
        "fsMountingPoint": partition.get_fs_mounting_point(),
        "fsLabel": partition.get_fs_label(),
        "fsFreeSize": partition.get_fs_free_size() * 512,
      }
    
    return str(datapartition)
