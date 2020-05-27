// Code generated by protoc-gen-go. DO NOT EDIT.
// source: server_status.proto

package proto

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

//@@.. cpp:var:: message SharedMemoryRegion
//@@
//@@   The meta-data for the shared memory region registered in the inference
//@@   server.
//@@
type SharedMemoryRegion struct {
	//@@
	//@@  .. cpp:var:: string name
	//@@
	//@@     The name for this shared memory region.
	//@@
	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	//@@  .. cpp:var:: oneof shared_memory_types
	//@@
	//@@     Types of shared memory identifiers
	//@@
	//
	// Types that are valid to be assigned to SharedMemoryTypes:
	//	*SharedMemoryRegion_SystemSharedMemory_
	//	*SharedMemoryRegion_CudaSharedMemory_
	SharedMemoryTypes isSharedMemoryRegion_SharedMemoryTypes `protobuf_oneof:"shared_memory_types"`
	//@@  .. cpp:var:: uint64 byte_size
	//@@
	//@@     Size of the shared memory block, in bytes.
	//@@
	ByteSize             uint64   `protobuf:"varint,5,opt,name=byte_size,json=byteSize,proto3" json:"byte_size,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SharedMemoryRegion) Reset()         { *m = SharedMemoryRegion{} }
func (m *SharedMemoryRegion) String() string { return proto.CompactTextString(m) }
func (*SharedMemoryRegion) ProtoMessage()    {}
func (*SharedMemoryRegion) Descriptor() ([]byte, []int) {
	return fileDescriptor_d1c8274bb4c3bd67, []int{0}
}

func (m *SharedMemoryRegion) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SharedMemoryRegion.Unmarshal(m, b)
}
func (m *SharedMemoryRegion) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SharedMemoryRegion.Marshal(b, m, deterministic)
}
func (m *SharedMemoryRegion) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SharedMemoryRegion.Merge(m, src)
}
func (m *SharedMemoryRegion) XXX_Size() int {
	return xxx_messageInfo_SharedMemoryRegion.Size(m)
}
func (m *SharedMemoryRegion) XXX_DiscardUnknown() {
	xxx_messageInfo_SharedMemoryRegion.DiscardUnknown(m)
}

var xxx_messageInfo_SharedMemoryRegion proto.InternalMessageInfo

func (m *SharedMemoryRegion) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

type isSharedMemoryRegion_SharedMemoryTypes interface {
	isSharedMemoryRegion_SharedMemoryTypes()
}

type SharedMemoryRegion_SystemSharedMemory_ struct {
	SystemSharedMemory *SharedMemoryRegion_SystemSharedMemory `protobuf:"bytes,2,opt,name=system_shared_memory,json=systemSharedMemory,proto3,oneof"`
}

type SharedMemoryRegion_CudaSharedMemory_ struct {
	CudaSharedMemory *SharedMemoryRegion_CudaSharedMemory `protobuf:"bytes,3,opt,name=cuda_shared_memory,json=cudaSharedMemory,proto3,oneof"`
}

func (*SharedMemoryRegion_SystemSharedMemory_) isSharedMemoryRegion_SharedMemoryTypes() {}

func (*SharedMemoryRegion_CudaSharedMemory_) isSharedMemoryRegion_SharedMemoryTypes() {}

func (m *SharedMemoryRegion) GetSharedMemoryTypes() isSharedMemoryRegion_SharedMemoryTypes {
	if m != nil {
		return m.SharedMemoryTypes
	}
	return nil
}

func (m *SharedMemoryRegion) GetSystemSharedMemory() *SharedMemoryRegion_SystemSharedMemory {
	if x, ok := m.GetSharedMemoryTypes().(*SharedMemoryRegion_SystemSharedMemory_); ok {
		return x.SystemSharedMemory
	}
	return nil
}

func (m *SharedMemoryRegion) GetCudaSharedMemory() *SharedMemoryRegion_CudaSharedMemory {
	if x, ok := m.GetSharedMemoryTypes().(*SharedMemoryRegion_CudaSharedMemory_); ok {
		return x.CudaSharedMemory
	}
	return nil
}

func (m *SharedMemoryRegion) GetByteSize() uint64 {
	if m != nil {
		return m.ByteSize
	}
	return 0
}

// XXX_OneofWrappers is for the internal use of the proto package.
func (*SharedMemoryRegion) XXX_OneofWrappers() []interface{} {
	return []interface{}{
		(*SharedMemoryRegion_SystemSharedMemory_)(nil),
		(*SharedMemoryRegion_CudaSharedMemory_)(nil),
	}
}

type SharedMemoryRegion_SystemSharedMemory struct {
	//@@  .. cpp:var:: string shared_memory_key
	//@@
	//@@     The name of the shared memory region that holds the input data
	//@@     (or where the output data should be written).
	//@@
	SharedMemoryKey string `protobuf:"bytes,1,opt,name=shared_memory_key,json=sharedMemoryKey,proto3" json:"shared_memory_key,omitempty"`
	//@@  .. cpp:var:: uint64 offset
	//@@
	//@@     This is the offset of the shared memory block from the start
	//@@     of the shared memory region.
	//@@     start = offset, end = offset + byte_size;
	//@@
	Offset               uint64   `protobuf:"varint,2,opt,name=offset,proto3" json:"offset,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SharedMemoryRegion_SystemSharedMemory) Reset()         { *m = SharedMemoryRegion_SystemSharedMemory{} }
func (m *SharedMemoryRegion_SystemSharedMemory) String() string { return proto.CompactTextString(m) }
func (*SharedMemoryRegion_SystemSharedMemory) ProtoMessage()    {}
func (*SharedMemoryRegion_SystemSharedMemory) Descriptor() ([]byte, []int) {
	return fileDescriptor_d1c8274bb4c3bd67, []int{0, 0}
}

func (m *SharedMemoryRegion_SystemSharedMemory) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SharedMemoryRegion_SystemSharedMemory.Unmarshal(m, b)
}
func (m *SharedMemoryRegion_SystemSharedMemory) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SharedMemoryRegion_SystemSharedMemory.Marshal(b, m, deterministic)
}
func (m *SharedMemoryRegion_SystemSharedMemory) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SharedMemoryRegion_SystemSharedMemory.Merge(m, src)
}
func (m *SharedMemoryRegion_SystemSharedMemory) XXX_Size() int {
	return xxx_messageInfo_SharedMemoryRegion_SystemSharedMemory.Size(m)
}
func (m *SharedMemoryRegion_SystemSharedMemory) XXX_DiscardUnknown() {
	xxx_messageInfo_SharedMemoryRegion_SystemSharedMemory.DiscardUnknown(m)
}

var xxx_messageInfo_SharedMemoryRegion_SystemSharedMemory proto.InternalMessageInfo

func (m *SharedMemoryRegion_SystemSharedMemory) GetSharedMemoryKey() string {
	if m != nil {
		return m.SharedMemoryKey
	}
	return ""
}

func (m *SharedMemoryRegion_SystemSharedMemory) GetOffset() uint64 {
	if m != nil {
		return m.Offset
	}
	return 0
}

type SharedMemoryRegion_CudaSharedMemory struct {
	//@@  .. cpp:var:: int64 device_id
	//@@
	//@@     The GPU device ID on which the cudaIPC handle was created.
	//@@
	DeviceId             int64    `protobuf:"varint,1,opt,name=device_id,json=deviceId,proto3" json:"device_id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SharedMemoryRegion_CudaSharedMemory) Reset()         { *m = SharedMemoryRegion_CudaSharedMemory{} }
func (m *SharedMemoryRegion_CudaSharedMemory) String() string { return proto.CompactTextString(m) }
func (*SharedMemoryRegion_CudaSharedMemory) ProtoMessage()    {}
func (*SharedMemoryRegion_CudaSharedMemory) Descriptor() ([]byte, []int) {
	return fileDescriptor_d1c8274bb4c3bd67, []int{0, 1}
}

func (m *SharedMemoryRegion_CudaSharedMemory) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SharedMemoryRegion_CudaSharedMemory.Unmarshal(m, b)
}
func (m *SharedMemoryRegion_CudaSharedMemory) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SharedMemoryRegion_CudaSharedMemory.Marshal(b, m, deterministic)
}
func (m *SharedMemoryRegion_CudaSharedMemory) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SharedMemoryRegion_CudaSharedMemory.Merge(m, src)
}
func (m *SharedMemoryRegion_CudaSharedMemory) XXX_Size() int {
	return xxx_messageInfo_SharedMemoryRegion_CudaSharedMemory.Size(m)
}
func (m *SharedMemoryRegion_CudaSharedMemory) XXX_DiscardUnknown() {
	xxx_messageInfo_SharedMemoryRegion_CudaSharedMemory.DiscardUnknown(m)
}

var xxx_messageInfo_SharedMemoryRegion_CudaSharedMemory proto.InternalMessageInfo

func (m *SharedMemoryRegion_CudaSharedMemory) GetDeviceId() int64 {
	if m != nil {
		return m.DeviceId
	}
	return 0
}

//@@
//@@.. cpp:var:: message SharedMemoryStatus
//@@
//@@   Shared memory status for the inference server.
//@@
type SharedMemoryStatus struct {
	//@@
	//@@  .. cpp:var:: SharedMemoryRegion shared_memory_region (repeated)
	//@@
	//@@     The list of active/registered shared memory regions.
	//@@
	SharedMemoryRegion   []*SharedMemoryRegion `protobuf:"bytes,2,rep,name=shared_memory_region,json=sharedMemoryRegion,proto3" json:"shared_memory_region,omitempty"`
	XXX_NoUnkeyedLiteral struct{}              `json:"-"`
	XXX_unrecognized     []byte                `json:"-"`
	XXX_sizecache        int32                 `json:"-"`
}

func (m *SharedMemoryStatus) Reset()         { *m = SharedMemoryStatus{} }
func (m *SharedMemoryStatus) String() string { return proto.CompactTextString(m) }
func (*SharedMemoryStatus) ProtoMessage()    {}
func (*SharedMemoryStatus) Descriptor() ([]byte, []int) {
	return fileDescriptor_d1c8274bb4c3bd67, []int{1}
}

func (m *SharedMemoryStatus) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SharedMemoryStatus.Unmarshal(m, b)
}
func (m *SharedMemoryStatus) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SharedMemoryStatus.Marshal(b, m, deterministic)
}
func (m *SharedMemoryStatus) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SharedMemoryStatus.Merge(m, src)
}
func (m *SharedMemoryStatus) XXX_Size() int {
	return xxx_messageInfo_SharedMemoryStatus.Size(m)
}
func (m *SharedMemoryStatus) XXX_DiscardUnknown() {
	xxx_messageInfo_SharedMemoryStatus.DiscardUnknown(m)
}

var xxx_messageInfo_SharedMemoryStatus proto.InternalMessageInfo

func (m *SharedMemoryStatus) GetSharedMemoryRegion() []*SharedMemoryRegion {
	if m != nil {
		return m.SharedMemoryRegion
	}
	return nil
}

func init() {
	proto.RegisterType((*SharedMemoryRegion)(nil), "nvidia.inferenceserver.SharedMemoryRegion")
	proto.RegisterType((*SharedMemoryRegion_SystemSharedMemory)(nil), "nvidia.inferenceserver.SharedMemoryRegion.SystemSharedMemory")
	proto.RegisterType((*SharedMemoryRegion_CudaSharedMemory)(nil), "nvidia.inferenceserver.SharedMemoryRegion.CudaSharedMemory")
	proto.RegisterType((*SharedMemoryStatus)(nil), "nvidia.inferenceserver.SharedMemoryStatus")
}

func init() { proto.RegisterFile("server_status.proto", fileDescriptor_d1c8274bb4c3bd67) }

var fileDescriptor_d1c8274bb4c3bd67 = []byte{
	// 310 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x92, 0x41, 0x4f, 0xfa, 0x40,
	0x10, 0xc5, 0xff, 0xa5, 0xfc, 0x09, 0x0c, 0x07, 0x71, 0x40, 0xd2, 0xe0, 0xa5, 0xe1, 0xd4, 0x70,
	0xa8, 0x09, 0x1e, 0x8d, 0x17, 0xb9, 0x68, 0x8c, 0x97, 0xed, 0xc5, 0x83, 0x49, 0x53, 0xba, 0x83,
	0x6e, 0x48, 0x5b, 0xdc, 0x59, 0x48, 0xca, 0x17, 0xf4, 0x6b, 0x19, 0x17, 0x0e, 0xb4, 0xe5, 0xa0,
	0xb7, 0xdd, 0xb7, 0x33, 0xf3, 0x7b, 0x79, 0xb3, 0x30, 0x64, 0xd2, 0x3b, 0xd2, 0x31, 0x9b, 0xc4,
	0x6c, 0x39, 0xdc, 0xe8, 0xc2, 0x14, 0x38, 0xce, 0x77, 0x4a, 0xaa, 0x24, 0x54, 0xf9, 0x8a, 0x34,
	0xe5, 0x29, 0x1d, 0x8a, 0xa6, 0x5f, 0x2e, 0x60, 0xf4, 0x91, 0x68, 0x92, 0x2f, 0x94, 0x15, 0xba,
	0x14, 0xf4, 0xae, 0x8a, 0x1c, 0x11, 0xda, 0x79, 0x92, 0x91, 0xe7, 0xf8, 0x4e, 0xd0, 0x13, 0xf6,
	0x8c, 0x9f, 0x30, 0xe2, 0x92, 0x0d, 0x65, 0x31, 0xdb, 0x86, 0x38, 0xb3, 0x1d, 0x5e, 0xcb, 0x77,
	0x82, 0xfe, 0xfc, 0x3e, 0x3c, 0x4f, 0x08, 0x9b, 0xd3, 0xc3, 0xc8, 0x8e, 0x39, 0x7d, 0x78, 0xfc,
	0x27, 0x90, 0x1b, 0x2a, 0xae, 0x01, 0xd3, 0xad, 0x4c, 0x6a, 0x40, 0xd7, 0x02, 0xef, 0xfe, 0x00,
	0x5c, 0x6c, 0x65, 0x52, 0xc3, 0x0d, 0xd2, 0x9a, 0x86, 0xd7, 0xd0, 0x5b, 0x96, 0x86, 0x62, 0x56,
	0x7b, 0xf2, 0xfe, 0xfb, 0x4e, 0xd0, 0x16, 0xdd, 0x1f, 0x21, 0x52, 0x7b, 0x9a, 0xbc, 0x02, 0x36,
	0x5d, 0xe3, 0x0c, 0x2e, 0x2b, 0xd6, 0xe2, 0x35, 0x95, 0xc7, 0xcc, 0x2e, 0xf8, 0xa4, 0xf0, 0x99,
	0x4a, 0x1c, 0x43, 0xa7, 0x58, 0xad, 0x98, 0x8c, 0x0d, 0xac, 0x2d, 0x8e, 0xb7, 0xc9, 0x0d, 0x0c,
	0x16, 0x67, 0xac, 0x48, 0xda, 0xa9, 0x94, 0x62, 0x25, 0xed, 0x3c, 0x57, 0x74, 0x0f, 0xc2, 0x93,
	0x7c, 0xb8, 0x82, 0x61, 0x15, 0x6a, 0xca, 0x0d, 0xf1, 0x54, 0x57, 0x17, 0x19, 0xd9, 0xed, 0xe3,
	0x1b, 0x8c, 0xaa, 0xc5, 0xda, 0x26, 0xe2, 0xb5, 0x7c, 0x37, 0xe8, 0xcf, 0x67, 0xbf, 0xcf, 0x50,
	0x20, 0x37, 0xb4, 0x65, 0xc7, 0x7e, 0xae, 0xdb, 0xef, 0x00, 0x00, 0x00, 0xff, 0xff, 0x2f, 0xb3,
	0xef, 0x11, 0x73, 0x02, 0x00, 0x00,
}
