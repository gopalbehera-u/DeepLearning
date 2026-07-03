import math

class Euclideandisttraker:
    def __init__(self):
        self.center_points={}
        self.id_count=0
    def update(self,object_rect):
        object_bbs_ids=[]
        for rect in object_rect:
            x,y,w,h=rect
            cx=(x+x+w)//2
            cy=(y+y+h)//2

            same_object_detection=False
            for id,pt in self.center_points.items():
                dist=math.hypot(cx-pt[0],cy-pt[1])
                if dist<50:
                    self.center_points[id]=(cx,cy)
                    print(self.center_points)
                    object_bbs_ids.append([x,y,w,h,id])
                    same_object_detection=True
                    break
            if same_object_detection is False:
                self.center_points[self.id_count]=(cx,cy)
                object_bbs_ids.append([x,y,w,h,self.id_count])
                self.id_count+=1
            
        new_center_points={}
        for obj_bb_id in object_bbs_ids:
            _,_,_,_,obj_id=obj_bb_id
            center=self.center_points[obj_id]
            new_center_points[obj_id]=center
    
        self.center_points=new_center_points.copy()
        return object_bbs_ids
    
    
 