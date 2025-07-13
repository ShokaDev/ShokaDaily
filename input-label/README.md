# Animated Input Label (Email & Password)

Simple HTML + CSS floating label form for both email and password fields.

## Features

- Floating label animation on input focus or when filled
- Clean design with smooth transitions
- No JavaScript required

## Fields

- Email
- Password

## How It Works

Using `position: absolute` and `transition`, the `<label>` floats up when:
- The input is focused

## Example

```html
<div class="group">
  <input type="email" required>
  <label>Email</label>
</div>
<div class="group">
  <input type="password" required>
  <label>Password</label>
</div>
```

## Styling

```css
label {
  position: absolute;
  top: 10px;
  left: 5px;
  transition: 0.3s ease all;
}
input:focus ~ label,
input:valid ~ label {
  top: -20px;
  font-size: 14px;
  color: #7700ff;
}
```