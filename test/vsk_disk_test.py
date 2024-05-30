import pytest
from unittest.mock import Mock, MagicMock
from Vasak.hardware.vsk_disks import VSKDisks

@pytest.fixture
def mock_disk():
    disk = Mock()
    disk.get_name.return_value = 'disk1'
    disk.get_device_id.return_value = 'device1'
    disk.get_model.return_value = 'model1'
    disk.get_partition_table_type.return_value = 'type1'
    disk.get_partition_table_uuid.return_value = 'uuid1'
    disk.get_path.return_value = '/path/to/disk1'
    disk.get_serial_number.return_value = 'serial1'
    disk.get_size.return_value = 1000
    disk.get_type_str.return_value = 'type_str1'
    return disk

@pytest.fixture
def mock_partition():
    partition = Mock()
    partition.get_part_scheme.return_value = 'gpt'
    partition.get_path.return_value = '/path/to/partition1'
    partition.get_name.return_value = 'partition1'
    partition.get_part_size.return_value = 500
    partition.get_part_offset.return_value = 0
    partition.get_part_number.return_value = 1
    partition.get_part_device_id.return_value = 'device1'
    partition.get_fs_version.return_value = '1.0'
    partition.get_fs_uuid.return_value = 'uuid1'
    partition.get_fs_usage.return_value = 'used'
    partition.get_fs_type.return_value = 'ext4'
    partition.get_fs_mounting_point.return_value = '/mount/point'
    partition.get_fs_label.return_value = 'label1'
    partition.get_fs_free_size.return_value = 250
    partition.get_part_uuid.return_value = 'uuid1'
    partition.get_part_label.return_value = 'label1'
    return partition

def test_partitionListToJSON(mock_partition):
    vsk_disks = VSKDisks()
    result = vsk_disks.partitionListToJSON([mock_partition])
    assert result is not None

def test_partitionToJSON(mock_partition):
    vsk_disks = VSKDisks()
    result = vsk_disks.partitionToJSON(mock_partition)
    assert result is not None