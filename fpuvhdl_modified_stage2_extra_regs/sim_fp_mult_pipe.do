
vcom -93 -work ./work ./common/fpnormalize_fpnormalize.vhd
vcom -93 -work ./work ./common/fpround_fpround.vhd
vcom -93 -work ./work ./common/packfp_packfp.vhd
vcom -93 -work ./work ./common/unpackfp_unpackfp.vhd  

vcom -93 -work ./work ./multiplier/fpmul_stage1_struct.vhd
vcom -93 -work ./work ./multiplier/fpmul_stage2_struct_modified_extra_regs.vhd
vcom -93 -work ./work ./multiplier/fpmul_stage3_struct.vhd
vcom -93 -work ./work ./multiplier/fpmul_stage4_struct.vhd
vcom -93 -work ./work ./multiplier/regnbit.vhd

vcom -93 -work ./work ./multiplier/fpmul_pipeline.vhd

vcom -93 -work ./work ./tb/clk_gen.vhd
vcom -93 -work ./work ./tb/data_sink.vhd
vcom -93 -work ./work ./tb/data_maker.vhd

vlog -work ./work ./tb/tb_mult_pipe.v

vsim work.tb_mult_pipe

add wave -r *

run 200 ns
