import pygame
import sys


white = 255,255,255
blue = 0,0,200


pygame.init()                       # 初始化pygame
pygame.mixer.init()					# 初始化音乐
file='music/bgmusic.mp3'		# 音乐的路径
track = pygame.mixer.music.load(file)	# 加载音乐文件
pygame.mixer.music.play(-1) #把play改成pause和unpause就可以实现暂停和继续播的功能。play(1,250)第一个参数：播放次数（n>0）,n=0时播放1次，-1是特殊值，会循环播放。执行的结果与书本上的结果不一致。
#第二个参数：从音乐开头250s开始播放音乐。
size = width, height = 640, 480     # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello Pygame", True, white)
ball = pygame.image.load('img/bgimg1.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    screen.fill(blue)
    #screen.blit(textImage, (200,200))
    screen.blit(ball, ballrect)
    pygame.display.update()
    #pygame.display.flip()  # 更新全部显示
#pygame.quit()  # 退出pygame
