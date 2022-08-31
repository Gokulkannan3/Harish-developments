class Image: 
    
    count=0

    def __init__(self,source,name="image",padding = {"top":"10px","right":"10px","bottom":"10px","left":"10px"},
                pos=["none"]*2,posMode="relative",radius="10px",margin={"left":"10px","right":"10px","top":"10px","bottom":"10px"},size=("25%","25%")):
            self.name=name+'-'+str(Image.count) if name=='image' else name
            self.source=source
            self.padding=padding
            self.pos=pos
            self.posMode=posMode
            self.radius=radius
            self.margin=margin
            self.size=size

    def style_generate(self):
        return(f"\n.{self.name}"+'{\n\t'
        "\n\t padding :"+ f"{self.padding.get('top','10px')} {self.padding.get('right','10px')} {self.padding.get('bottom','10px')} {self.padding.get('left','10px')}:\n\t"
        "position :"+ f"{self.posMode};\n\t"
        "left :"+ f"{self.pos[0]};\n\t"
        "top :"+ f"{self.pos[-1]};\n\t"
        "radius :"+f"{self.radius};\n\t"
        "margin :"+ f"{self.margin.get('top','10px')} {self.margin.get('right','10px')} {self.margin.get('bottom','10px')} {self.margin.get('left','10px')};\n\t"
        "width :"+ f"{self.size[0]};\n\t"
        "height :"+ f"{self.size[-1]};\n\t"
        '}\n'
               
        ) 
    
    def function_generate(self):
        return
    
    def self_generate(self):
        return(f"""\n<img classs="{self.name}"src="{self.source}/>""")
    

if __name__=="__main__":
        
    image=Image(source=r"C:\Users\gokul\OneDrive\Pictures\Saved Pictures\food.jpg")
        
    print(image.self_generate())
        
    print(image.style_generate())
