import pygame as pg

COLOR = 'magenta'


# FONT = pg.font.SysFont('Corbel', 32)
def get_font(font='Corbel', size=32):
    pg.font.init()
    return pg.font.SysFont(font, size)


class InpBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR
        self.text = text
        self.txt_surface = get_font().render(text, True, self.color)
        self.active = False
        self.value = None
        # self.original = self.text

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:

            # if user click on input_box rect
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_KP_ENTER:

                    return_text = self.get_input(self.text)
                    print(return_text)
                    self.value = return_text
                    self.text = ''
                    return self.value

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # Re-render the text
                self.txt_surface = get_font().render(self.text, True, self.color)

    def update(self):
        # Resize box if text too long
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # blit text
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

        # blit rect
        pg.draw.rect(screen, self.color, self.rect, 2)

    def get_input(self, text):
        if text.isnumeric():
            return int(text)
        else:
            pass


if __name__ == "__main__":
    box = InpBox(100, 100, 140, 32)
    print(box.get_input())
