
vcom -93 -work ./work ../src/mux_4to1_nbit.vhd
vcom -93 -work ./work ../src/MBE_encoder.vhd

vcom -93 -work ./work ./tb/clk_gen.vhd
vcom -93 -work ./work ./tb/data_sink.vhd
vcom -93 -work ./work ./tb/data_maker.vhd

vlog -work ./work ./tb/tb_MBE_encoder.v

vsim work.tb_MBE_encoder

add wave -r *
run 100 ns
