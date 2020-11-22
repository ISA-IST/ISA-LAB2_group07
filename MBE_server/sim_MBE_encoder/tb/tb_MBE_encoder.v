//`timescale 1ns

module tb_MBE_encoder ();

   wire CLK_i;
   //wire RST_n_i;
   wire [31:0] A;
   wire [32:0] pp;
   wire        b2, b1, b0;
   
  
  
   clk_gen CG(.CLK(CLK_i));
	      

   data_maker SM(.CLK(CLK_i),		 
		 .A(A),
		 .b0(b0),
		 .b1(b1),
		 .b2(b2));

   MBE_encoder UUT(
		   .A(A),
		   .b0(b0),
		   .b1(b1),
		   .b2(b2),
		   .pp(pp));

   data_sink DS(.CLK(CLK_i),
		.pp(pp));

endmodule
