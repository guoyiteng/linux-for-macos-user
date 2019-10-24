store.set_global_value('hotkey', '<meta>+v')
if re.match('.*(Hyper)', window.get_active_class()):
    logging.debug('terminal')
    engine.set_return_value('<ctrl>+<shift>+v')
else:
    logging.debug('normal')
    engine.set_return_value('<ctrl>+v')
engine.run_script('combo')
