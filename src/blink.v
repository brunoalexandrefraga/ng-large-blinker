module blink(
    input clk,
    output led
    );
    
    reg [26:0] count = 0;
 
    assign led = count[26];
     
    always @ (posedge(clk)) begin
        count <= count + 1;
    end
endmodule