store.set_global_value('hotkey', '<meta>+t')
if re.match('.*(Hyper)', window.get_active_class()):
    logging.debug('terminal')
    engine.set_return_value('<ctrl>+<shift>+t')
else:
    logging.debug('normal')
    engine.set_return_value('<ctrl>+t')
engine.run_script('combo')