# 导出依赖包
`pip freeze > requirements.txt`

# 安装依赖
`pip install -r requirements.txt`

# 关键API
- `pygame.display.init` — 初始化display模块
- `pygame.display.quit` — 取消初始化display模块
- `pygame.display.get_init` — 如果display模块被初始化时返回True
- `pygame.display.set_mode` — 初始化一个准备显示的窗口或屏幕
- `pygame.display.get_surface` — 获取当前显示的Surface对象
- `pygame.display.flip` — 将完整带显示的Surface对象更新到屏幕上
- `pygame.display.update` — 更新部分软件界面显示
- `pygame.display.get_driver` — 获取pygame 显示后端的名称
- `pygame.display.Info` — 创建有关显示界面的信息对象
- `pygame.display.get_wm_info` — 获取有关当前窗口系统的信息
- `pygame.display.list_modes` — 获取可用全屏模式分辨率的列表
- `pygame.display.mode_ok` — 选择显示模式的最佳颜色深度
- `pygame.display.gl_get_attribute` — 获取当前显示界面的OpenGL属性（flag）的值
- `pygame.display.gl_set_attribute` — 请求当前显示模式的OpenGL属性值
- `pygame.display.get_active` — 当前显示界面显示在屏幕上时返回True
- `pygame.display.iconify` — 最小化显示的Surface对象
- `pygame.display.toggle_fullscreen` — 切换全屏显示和窗口显示
- `pygame.display.set_gamma` — 更改硬件显示的伽马（gama）坡道
- `pygame.display.set_gamma_ramp` — 自定义修改硬件显示的伽马坡道
- `pygame.display.set_icon` — 更改显示窗口的系统图像
- `pygame.display.set_caption` — 设置当前窗口标题
- `pygame.display.get_caption` — 获取当前窗口标题
- `pygame.display.set_palette` — 为索引显示设置显示调色板

这个模块提供了对pygame 显示界面的控制。Pygame的 Surface 对象即可显示为一个窗口，可以包含在窗口中，也可以全屏运行。当你创建并显示一个常规的 Surface 对象后，屏幕上无法立即看到更改;您必须从两个翻转（flipping）函数中选择一个来更新实际改动后得到画面。
显示（display）的原点（x = 0和y = 0）位于屏幕的左上角。两个轴都朝向屏幕的右下方正向增加。
Pygame的 display实际上可以有几种初始化的方式。默认情况下，display作为一个软件驱动的帧缓冲区。除此之外，您可以请求硬件加速和OpenGL支持等特殊模块。这些由传递给pygame.display.set_mode()的属性(flags)控制。
Pygame在任何时候都只能激活一个显示界面。使用pygame.display.set_mode()创建一个新的将关闭之前的显示界面。如果需要对像素格式或显示分辨率进行精确控制，请使用函数pygame.display.mode_ok()，pygame.display.list_modes()和 pygame.display.Info()来查询有关显示界面的信息。
一旦 Surface 对象的显示界面被创建出来，此模块中的函数将影响单个现有显示界面。如果模块未初始化，则Surface将变为无效。如果设置了新的显示模式，现有的Surface对象将自动切换到新的显示界面上。
当设置显示模式后，pygame事件队列（event queue）中会放置几个相关事件。当用户请求程序关闭时发送pygame.QUIT事件。当显示界面获得并失去输入焦点时，窗口将接收pygame.ACTIVEEVENT事件。如果使用pygame.RESIZABLE属性（flags）设置显示界面，则在用户调整窗口尺寸时将发送pygame.VIDEORESIZE事件。硬件显示指当接收到 pygame.VIDEOEXPOSE事件时，将部分需要被重绘的窗口直接绘制到屏幕上。
某些显示环境具有自动拉伸（automatically stretching）所有窗口的选项。当启用此选项后，此自动拉伸会扭曲pygame窗口的外观。在pygame的例子目录中，有一个示例代码（prevent_display_stretching.py），它显示了如何在微软系统（Vista 以上系统）中关闭 Pygame 显示的自动拉伸属性。
 

# 初始化display模块
pygame.display.init ↶
int() -> None
初始化pygame 的display模块。 在初始化之前，display模块无法执行任何操作。 当你调用更高级别的pygame.init()时，通常会自动处理这个问题。
Pygame会在初始化时从几个内部显示后端中选择一个。 将根据当前用户的平台和权限选择显示模式。 在初始化display模块之前，可以设置环境变量SDL_VIDEODRIVER来控制使用哪个后端。 此处列出了具有多个选项的系统（多个显示后端的系统）。
Windows : windib, directx
Unix : x11, dga, fbcon, directfb, ggi, vgl, svgalib, aalib
在某些平台上，可以将pygame 的display嵌入到现有窗口中。 为此，必须将环境变量SDL_WINDOWID设置为包含窗口ID或句柄的字符串。 初始化pygame 的display时，将检查环境变量。 请注意，在一个运行的窗口嵌入display可能会出现许多奇怪的副作用。
多次调用它是无害的，重复调用没有效果。
搜索pygame.display.init的示例

# 取消初始化display模块
pygame.display.quit ↶
quit() -> None
这将关闭整个display模块。 这意味着将关闭任何活跃的显示器。程序退出时也会自动处理。
多次调用它是无害的（没有任何问题），重复调用没有效果。
搜索pygame.display.quit的示例

# 如果display模块被初始化时返回True
pygame.display.get_init ↶
get_init() -> bool
如果当前pygame.display模块被初始化，返回True
搜索pygame.display.get_init的示例

#初始化窗口或屏幕以进行显示（display）
pygame.display.set_mode ↶
set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
（resolution -> 分辨率）
这个函数将创建一个Surface对象。传入的参数是对显示类型的请求。实际创建的显示将是系统支持的最佳匹配。
resolution参数是一对表示宽度和高度的数字。flags参数是其他选项的集合。depth参数表示用于颜色的位数。
返回的Surface对象可以像常规Surface对象一样绘制，但发生的改变最终会显示到屏幕上。
如果没有传递分辨率或设置为（0,0）并且pygame使用SDL版本1.2.10或更高版本，则创建的Surface将具有与当前屏幕分辨率相同的大小。如果仅将宽度或高度设置为0，则Surface对象将具有与屏幕分辨率相同的宽度或高度。使用1.2.10之前的SDL版本将引发异常。
通常最好不要传递深度（depth）参数。它将默认为系统的最佳和最快颜色深度。如果您的游戏需要特定的颜色格式，您可以使用此参数控制深度。 Pygame 将为模拟一个非现成的颜色深度而耗费更多的时间。
请求全屏显示模式时，有时无法完全匹配所请求的分辨率。在这些情况下，pygame将选择最接近的兼容匹配。返回的surface仍将始终与请求的分辨率匹配。
flags参数控制您想要的显示类型。有几种可供选择，您甚至可以使用按位或运算符（管道“|”字符）组合多种类型。如果传递0或没有flags参数，它将默认为软件驱动的窗口。以下是您要选择的显示标志：
`pygame.FULLSCREEN`创建一个全屏显示
`pygame.DOUBLEBUF` 1.双缓冲模式 2.推荐和`HWSURFACE`或`OPENGL`一起使用
`pygame.HWSURFACE`硬件加速，仅在FULLSCREEN下可以使用
`pygame.OPENGL`创建一个OpenGL可渲染的显示器
`pygame.RESIZABLE`创建一个可调整尺寸的窗口
`pygame.NOFRAME`创建一个没有边框和控制按钮的窗口

例如：
在屏幕中创建一个 700 * 400 的窗口
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])

# 获取当前显示的 Surface 对象。
pygame.display.get_surface ↶
get_surface() -> Surface
返回对当前显示的Surface对象。如果未设置任何显示模式，则返回None。

# 将完整待显示的Surface对象更新到屏幕上
pygame.display.flip ↶
flip() -> None
这将更新整个显示器的内容。如果你的显示器模式使用标志pygame.HWSURFACE（硬件加速）和pygame.DOUBLEBUF（双缓冲），这将等待垂直会扫（vertical retrace）并切换显示界面。 如果你使用不同类型的显示模式，那么它将简单的更新整个显示界面的内容。
使用pygame.OPENGL（使用OPENGL渲染）显示模式时，这将执行gl缓冲区交换。
小甲鱼温馨提示：垂直回扫是与视频显示相关的时间测量，它代表了一个帧的结束和下一帧的开始时间之间的时间间隔。

# 更新部分软件界面显示
pygame.display.update ↶
update(rectangle=None) -> None
update(rectangle_list) -> None
这个函数可以看作是 pygame.display.flip() 函数在软件界面显示的优化版。 它只允许更新屏幕的一部分，而不是整个区域。 如果没有传递参数，它会就像pygame.display.flip()一样更新整个Surface区域。

您可以传递一个或多个矩形给这个函数。 一次传递多个矩形比使用单个或部分矩形列表多次调用更新更有效。 如果传递多个矩形，在列表中包含None值是安全的，那么将会被忽略。
此调用不能用于pygame.OPENGL显示模式下，否则将生成异常。

# 获取pygame 显示后端的名称
pygame.display.get_driver ↶
get_driver() -> name
Pygame在初始化时选择许多可用的显示后端之一。 这函数将返回用于显示后端的内部名称。 这可用于提供有关可能加速的显示功能的有限信息。 请参阅pygame.display.set_mode()中的SDL_VIDEODRIVER标志以查看一些常用选项。

# 创建视频显示信息对象
pygame.display.Info ↶
Info() -> VideoInfo
创建一个对象，包含对当前图形环境一些属性的描述。 如果在pygame.display.set_mode()之前调用它，某些平台可以提供有关默认显示模式的信息。 也可以在设置完显示模式后调用该函数，以确认显示选项是否如愿以偿。 VidInfo对象将包含以下这些属性：
`hw`：如果是 True，则表示启用硬件加速
`wm`：如果是 True，则表示显示窗口模式
`video_mem`：表示显存是多少兆字节（mb）。如果未知，则为0
`bitsize`：表示每个像素存放多少位
`bytesize`：表示每个像素存放多少字节
`masks`：4 个值用于打包像素的 RGBA 值
`shifts`：4 个值用于打包像素的 RGBA 值值
`losses`：4 个值用于打包像素的 RGBA 值
`blit_hw`：如果是 True，则表示加速硬件驱动的 Surface 对象绘制
`blit_hw_CC`：如果是 True，则表示加速硬件驱动的 Surface 对象 colorkey 绘制
`blit_hw_A`：如果是 True，则表示加速硬件驱动的 Surface 对象 pixel alpha 绘制
`blit_sw`：如果是 True，则表示加速软件驱动的 Surface 对象绘制
`blit_sw_CC`：如果是 True，则表示加速软件驱动的 Surface 对象 colorkey 绘制
`blit_sw_A`：如果是 True，则表示加速软件驱动的 Surface 对象 pixel alpha 绘制
`current_h`，`current_w`：

表示当前显示模式的宽和高（如果在 display.set_mode() 前被调用，则表示当前桌面的宽和高）
current_w, current_h 在 Pygame 1.8.0 以后，SDL 1.2.10 以后才支持
-1 表示错误，或者 SDL 版本太旧

# 获取有关当前窗口系统的信息
pygame.display.get_wm_info ↶
get_wm_info() -> dict
创建一个由操作系统填充数据的字典。 字符串和值由系统任意创建。 某些系统可能没有信息，将返回空字典。 大多数平台将返回一个“窗口”键，其值设置为当前显示的系统ID。
新的pygame 1.7.1

# 获取可用全屏模式可用的分辨率列表
pygame.display.list_modes ↶
list_modes(depth=0, flags=pygame.FULLSCREEN) -> list
此函数返回指定颜色深度的所支持的所有分辨率的列表。 如果给定参数没有可用的显示模式，则返回值将为空列表。 返回值为-1表示任何请求的分辨率都应该有效（对于窗口模式可能就是这种情况）。 模式大小从最大到最小排序。
如果深度为0，SDL将为显示器选择当前/最佳颜色深度。 属性（flags）默认为pygame.FULLSCREEN，但您可能需要为特定的全屏模式添加其他标志。

# 选择显示模式的最佳颜色深度
pygame.display.mode_ok ↶
mode_ok(size, flags=0, depth=0) -> depth
此函数使用与pygame.display.set_mode()相同的参数。 它用于确定所请求的显示模式是否可用。 如果无法设置显示模式，它将返回0。 否则，它将返回与所要求的显示最匹配的像素深度。
通常不用理会深度参数，但某些平台可以支持多个显示深度。 如果传递此参数将暗示哪个深度是更好的匹配。
要传递的最有用的标志是pygame.HWSURFACE，pygame.DOUBLEBUF，也许是pygame.FULLSCREEN。 如果无法设置这些显示标志，该函数将返回0。

# 获取当前显示界面的OpenGL属性（flag）的值
pygame.display.gl_get_attribute ↶
gl_get_attribute(flag) -> value
在使用pygame.OPENGL标志调用pygame.display.set_mode()之后，最好检查任何请求的OpenGL属性的值。 有关有效标志的列表，请参阅pygame.display.gl_set_attribute()。

# 设置当前显示模式的 OpenGL 属性值。
pygame.display.gl_set_attribute ↶
gl_set_attribute(flag, value) -> None
当使用pygame.OPENGL标志调用pygame.display.set_mode()时，Pygame会自动处理设置OpenGL属性，如颜色和双缓冲区。 OpenGL提供了一些您可能想要控制的其他属性。 将其中一个属性作为标志及其适当的值传递。 这必须在pygame.display.set_mode()之前调用
这些OPENGL标志是：
GL_ALPHA_SIZE, GL_DEPTH_SIZE, GL_STENCIL_SIZE, GL_ACCUM_RED_SIZE,
GL_ACCUM_GREEN_SIZE, GL_ACCUM_BLUE_SIZE, GL_ACCUM_ALPHA_SIZE,
GL_MULTISAMPLEBUFFERS, GL_MULTISAMPLESAMPLES, GL_STEREO

# 当display在显示中处于活跃状态时返回True
pygame.display.get_active ↶
get_active() -> bool
调用pygame.display.set_mode()后，Surface对象将被显示在屏幕上。 大多数窗口显示都可以被用户隐藏。 如果显示器Surface隐藏或最小化，则返回False。

# 最小化显示Surface对象
pygame.display.iconify ↶
iconify() -> bool
将显示的 Surface 对象最小化或隐藏。 并非所有系统和显示器都支持最小化显示。 如果该函数调用成功，该函数将返回True。
当显示器最小化时，pygame.display.get_active()将返回False。 当窗口已最小化时，事件队列应接收ACTIVEEVENT事件。

# 在全屏和窗口模式之间切换
pygame.display.toggle_fullscreen ↶
toggle_fullscreen() -> bool
在窗口模式和全屏模式之间切换显示窗口。 此函数仅适用于UNIX X11显示驱动程序。 在大多数情况下，建议调用 pygame.display.set_mode() 创建一个新的显示模式进行切换。

# 修改硬件显示的伽马坡道。
pygame.display.set_gamma ↶
set_gamma(red, green=None, blue=None) -> bool
在硬件驱动显示上设置红色，绿色和蓝色伽玛值。 如果未传递green和blue参数，则它们将与red相等。 并非所有系统和硬件都支持伽马坡道，如果函数修改成功，它将返回True。
伽玛值为1.0会创建线性颜色表。 较低的值会使屏幕变暗，较高的值会变亮。

# 自定义修改硬件显示的 伽马坡道
pygame.display.set_gamma_ramp ↶
set_gamma_ramp(red, green, blue) -> bool
使用自定义表（explicit lookup table）设置硬件驱动显示的红色，绿色和蓝色伽马坡道。 个参数必须是 256 位整数的列表。 整数应介于0和0xffff之间。 不是所有的操作系统和硬件都支持伽马坡道。如果函数修改成功，则返回 True。

# 更改显示窗口的图标
pygame.display.set_icon ↶
set_icon(Surface) -> None
设置系统将用于表示显示窗口（display window）的运行时图标。 所有窗口默认为窗口图标的简单pygame logo。
你可以传递任何surfacee对象作为图标，但大多数操作系统要求图标的大小是 32 * 32。 图像可以具有colorkey透明度，该透明度将传递给系统。
一些操作系统不允许修改显示中的窗口图标。对于这类操作系统，该函数需要再调用 pygame.display.set_mode() 前先创建并设置图标。

# 设置当前窗口标题栏
pygame.display.set_caption ↶
set_caption(title, icontitle=None) -> None
如果显示器有窗口标题，则此功能将更改窗口上的名称。 一些操作系统支持最小化窗口时切换标题栏，通过设置 icontitle 参数实现。

# 获取当前窗口标题
pygame.display.get_caption ↶
get_caption() -> (title, icontitle)
返回当前窗口的标题栏和最小化标题栏。这些通常是相同的值。

# 设置显示界面的调色板。
pygame.display.set_palette ↶
set_palette(palette=None) -> None
这个函数将修改显示界面的 8 位调色板。这不会更改实际Surface对象的调色板，仅用于Surface对象的显示。 如果未传递palette参数，则将还原系统默认调色板。 调色板是一系列RGB三元组。
