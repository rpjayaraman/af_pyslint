module memory(
    address,
    data_in,
    data_out,
    read_write,
    chip_en
  );

  input wire [7:0] address, data_in;
  output reg [7:0] data_out;
  input wire read_write, chip_en;

endmodule
