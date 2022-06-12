def center_target(target):
    xoffset = target.xoffset
    yoffset = target.yoffset
    
    if yoffset == 0:
        return 'stabilized'
    elif yoffset < 0:
        return 'move up'
    else:
        return 'move down'