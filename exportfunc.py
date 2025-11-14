import idaapi
import idc
import ida_hexrays
import os
import idautils
import ida_auto
import ida_pro
import ida_lines

ida_auto.auto_wait()

if not ida_hexrays.init_hexrays_plugin():
    print("check your license")
    ida_pro.qexit(1)

output_dir = r"C:\Users\DriverExport"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

export_count = 0
fail_count = 0

for ea in idautils.Functions():
    func_name = idc.get_func_name(ea)
    if not func_name:
        func_name = f"func_{hex(ea)}"
    
    safe_name = "".join(c for c in func_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    filename = f"{safe_name}.txt"
    filepath = os.path.join(output_dir, filename)
    
    hf = ida_hexrays.hexrays_failure_t()
    cfunc = ida_hexrays.decompile(ea, hf)

    if cfunc is None:
        print(f"Decompile başarısız ({fail_count + 1}): {func_name} ({hex(ea)}) - Sebep: {hf.str}")
        fail_count += 1
        continue
    
    pseudocode = cfunc.get_pseudocode()
    if not pseudocode:
        print(f"Pseudocode empty: {func_name} ({hex(ea)})")
        fail_count += 1
        continue

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            for line_idx in range(len(pseudocode)):
                line_obj = pseudocode[line_idx]
                line_text = ida_lines.tag_remove(line_obj.line)
                f.write(line_text + '\n')
        
        export_count += 1
        print(f"Exported ({export_count}): {filename}")
    except Exception as e:
        print(f"Write error ({fail_count + 1}): {func_name} - {str(e)}")
        fail_count += 1
        continue

print(f"DONE! SUCCESS: {export_count}, Başarısız: {fail_count}. Klasör: {output_dir}")
