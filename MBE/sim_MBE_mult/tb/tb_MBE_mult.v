//`timescale 1ns

module tb_MBE_mult ();

   wire CLK_i;
   //wire RST_n_i;
   wire [31:0] DIN_a;
   wire [31:0] DIN_b;
   wire [63:0] DOUT_i;
  
  
   clk_gen CG(.CLK(CLK_i));
	      

   data_maker SM(.CLK(CLK_i),		 
		 .DATA_a(DIN_a),
		 .DATA_b(DIN_b));

   MBE_mult UUT(
	    .A(DIN_a),
	    .B(DIN_b),
            .M(DOUT_i));

   data_sink DS(.CLK(CLK_i),
		.DIN(DOUT_i));

endmodule
