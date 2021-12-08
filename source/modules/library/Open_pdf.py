# Method 3: Open with webbrowser
import webbrowser
from modules.modules_math.math_analysis import *

    # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
if 0.8*compression_pressure < Pmax < compression_pressure*1.1 and 0.8*Minimum_pressure_intake < Pmin < Minimum_pressure_intake*1.1:
    value = 'Bình thường'
else:
    value = 'Hư hỏng'
    path_open = "F:\HK211\Luận Văn\source\library\libary_fix\Tháo lắp động cơ.pdf"
    if Pmax < Minimum_pressure:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Gãy xéc măng, gãy xupap lủng piston.pdf'
    elif Minimum_pressure < Pmax <0.62*compression_pressure:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Hở giăng nắp máy.pdf'
    elif 0.62*compression_pressure < Pmax <0.8*compression_pressure:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Hở xupap.pdf'
    elif Pmax > compression_pressure:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Xilanh không đều.pdf'
    elif Pmax > 0.9*compression_pressure:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Xilanh không đều.pdf'
    elif Pmin < 0.8*Minimum_pressure_intake:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Hở xupap.pdf'
    elif Pmin > 0.62*Minimum_pressure_intake:
        path = 'F:\HK211\Luận Văn\source\library\libary_fix\Hở giăng nắp máy.pdf'

webbrowser.open_new(path_open)
webbrowser.open_new(path)